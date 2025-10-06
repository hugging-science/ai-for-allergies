import time
from pathlib import Path
import html
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional
import re

try:
    import polars as pl
except Exception:
    raise

try:
    import requests
    from bs4 import BeautifulSoup
except Exception:
    # We'll only require these if the user enables URL validation/metadata fetching.
    requests = None
    BeautifulSoup = None

# Shared CSS for generated tables — emitted once into README so styles are centralized
TABLE_CSS = """
table, th, td { border: 3px solid #777; }
table { width: 100%; }
th.name { width:10%; }
th.description { width:75%; }
th.source { width:5%; }
th.license { width:5%; }
th.tags { width:5%; }
td.plain { color:#000000; }
/* Legend styles */
.legend { margin:8px 0 16px 0; font-size:90%; }
.legend .item { display:inline-flex; align-items:center; margin-right:12px; }
.legend .swatch { width:14px; height:14px; border:1px solid #ccc; margin-right:6px; display:inline-block; }
"""


def normalize_col(df, possible_names):
    """Return the first column name found in df.columns from possible_names, or None."""
    cols = df.columns
    for name in possible_names:
        if name in cols:
            return name
    return None


def availability_color(avail: str) -> str:
    """Map availability text to a hex background color."""
    if not avail:
        return "#ffffff"
    a = avail.strip().lower()
    if "open" in a:
        return "#e6ffea"  # light green
    else:
        return "#f7d6d6"  # light red

def make_link(text: str, url: str) -> str:
    if not url:
        return html.escape(text or "")
    return f'<a href="{html.escape(url)}">{html.escape(text or url)}</a>'


def is_url_like(s: Optional[str]) -> bool:
    if not s:
        return False
    s = s.strip()
    return s.startswith("http://") or s.startswith("https://")


def validate_url(url: str, timeout: int = 6) -> str:
    """Return a short status like '200 OK' or 'ERR: timeout'"""
    if requests is None:
        return "validation-unavailable"
    try:
        r = requests.head(url, allow_redirects=True, timeout=timeout)
        return f"{r.status_code} {r.reason or ''}".strip()
    except requests.exceptions.RequestException as e:
        # fallback to GET for servers that don't respond to HEAD
        try:
            r = requests.get(url, stream=True, timeout=timeout)
            return f"{r.status_code} {r.reason or ''}".strip()
        except Exception as e2:
            return f"ERR: {type(e).__name__}"


def fetch_metadata(url: str, timeout: int = 8) -> dict:
    """Return {'title':..., 'description':...} or empty dict on failure."""
    if requests is None or BeautifulSoup is None:
        return {}
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        desc_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        description = desc_tag.get("content", "").strip() if desc_tag and desc_tag.get("content") else ""
        return {"title": title, "description": description}
    except Exception:
        return {}


def render_table(rows, cols):
    """Render an HTML table given rows (list of dicts) and cols (list of (key,label))."""
    table = ['<table>']
    
    # header with small padding
    ths = []
    table.append('  <thead>')
    for _, label in cols:
        # width is per-column preference (kept inline because it depends on column order)
        ths.append(f'<th class="{label.lower()}">{html.escape(label)}</th>')
    table.append('    <tr>')
    table.append("      " + '\n      '.join(ths))
    table.append('    </tr>')
    table.append('  </thead>')
    table.append("  <tbody>")
    for r in rows:
        color = availability_color(r.get("Availability", ""))
        table.append(f'    <tr style="background-color:{color}">')
        for key, _ in cols:
            val = r.get(key, "") or ""
            # If the cell contains a link (<a ...>) we'll leave the link styling alone.
            # Otherwise, force black text color so it's readable regardless of theme.
            has_link = "<a " in val
            # add small padding and keep text wrapping for Description
            if has_link:
                table.append(f'      <td>{val}</td>')
            else:
                table.append(f'      <td class="plain">{val}</td>')
        table.append('    </tr>')
    table.append("  </tbody>")
    table.append("</table>\n")
    return "\n".join(table)


def render_legend() -> str:
    """Return an HTML legend for Availability colors."""
    items = [
        ("#e6ffea", "Open source"),
        ("#f7d6d6", "Gated"),
        ("#ffffff", "Unknown")
    ]
    parts = ["<div class=\"legend\">"]
    for color, label in items:
        parts.append(f'<span class="item"><span class="swatch" style="background:{color}"></span>{html.escape(label)}</span>')
    parts.append("</div>\n")
    return "\n".join(parts)


def remove_old_style_legend(readme_path: Path) -> None:
    """Remove previously-generated <style>...</style> blocks and legend divs from an existing README.

    This helps avoid mixing old inline/CSS blocks with the newly-generated one.
    """
    if not readme_path.exists():
        return
    text = readme_path.read_text(encoding="utf8")
    cleaned = re.sub(r"(?is)<style.*?>.*?</style>\s*", "", text)
    cleaned = re.sub(r"(?is)<div\s+class=[\"']legend[\"'].*?>.*?</div>\s*", "", cleaned)
    if cleaned != text:
        readme_path.write_text(cleaned, encoding="utf8")


def enrich_urls(records, validate: bool = False, fetch: bool = False, workers: int = 6) -> None:
    """Validate URLs and optionally fetch metadata. Mutates the records in-place.

    - validate: run HTTP HEAD/GET and attach small status strings to Source
    - fetch: fetch page title and description and attach to Source
    """
    if not (validate or fetch):
        return

    if requests is None or BeautifulSoup is None:
        # Dependencies not installed; do nothing but annotate accordingly if validating
        for r in records:
            chosen = r.get("_paper_url") or r.get("_source_url") or ""
            if chosen and validate:
                r["Source"] = r.get("Source", "") + f"<br><small>Status: validation-unavailable</small>"
        return

    urls = set()
    for r in records:
        if r.get("_source_url"):
            urls.add(r.get("_source_url"))
        if r.get("_paper_url"):
            urls.add(r.get("_paper_url"))

    if not urls:
        return

    url_status = {}
    url_meta = {}

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {}
        for u in urls:
            if validate:
                futures[ex.submit(validate_url, u)] = (u, "status")
            if fetch:
                futures[ex.submit(fetch_metadata, u)] = (u, "meta")

        for fut in as_completed(futures):
            u, kind = futures[fut]
            try:
                res = fut.result()
            except Exception:
                res = {}
            if kind == "status":
                url_status[u] = res
            else:
                url_meta[u] = res

    # Enrich the readable Source cell per-record
    for r in records:
        parts = [r.get("Source", "")]
        chosen = r.get("_paper_url") or r.get("_source_url") or ""
        if chosen:
            if validate:
                st = url_status.get(chosen, "")
                if st:
                    parts.append(f"<br><small>Status: {html.escape(str(st))}</small>")
            if fetch:
                m = url_meta.get(chosen, {}) or {}
                title = m.get("title") if isinstance(m, dict) else ""
                desc = m.get("description") if isinstance(m, dict) else ""
                if title:
                    parts.append(f"<br><small>Title: {html.escape(title)}</small>")
                if desc:
                    short = (desc[:200] + "...") if len(desc) > 200 else desc
                    parts.append(f"<br><small>{html.escape(short)}</small>")
        r["Source"] = "".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Generate README.md from datasets_spreadsheet.tsv")
    parser.add_argument("--validate-urls", action="store_true", help="Validate Source/Paper URLs (HTTP status)")
    parser.add_argument("--fetch-metadata", action="store_true", help="Fetch page title/description for Source/Paper URLs")
    parser.add_argument("--workers", type=int, default=6, help="Number of concurrent workers for HTTP requests")
    args = parser.parse_args()

    start_time = time.time()
    root = Path(__file__).parent
    tsv = root / "datasets_spreadsheet.tsv"
    if not tsv.exists():
        print(f"ERROR: dataset file not found at {tsv}")
        return

    # Read TSV (tab separated)
    df = pl.read_csv(str(tsv), separator="\t", try_parse_dates=False, null_values=["", "NA", "None"])  # keep as strings
    # Normalize column names (some files use slightly different headers)
    name_col = normalize_col(df, ["Name", "name"])
    cat_col = normalize_col(df, ["Category", "Categories", "category", "categories"])
    desc_col = normalize_col(df, ["Description", "description", "Summary", "summary"])
    source_col = normalize_col(df, ["Source", "source", "Data_Type", "Source URL"])
    paper_col = normalize_col(df, ["Paper link", "Paper Link", "paper link", "paper_link", "Link"])
    avail_col = normalize_col(df, ["Availability", "availability"])
    tags_col = normalize_col(df, ["Task", "Tags", "Task/Tags", "task", "Tags "]) or ""

    # Fallback to column names expected later
    if not name_col:
        raise RuntimeError("No Name column found in TSV")
    if not cat_col:
        cat_col = ""  # put in uncategorized

    # Convert to list of dicts and normalize
    df = df.fill_null("")
    records = []
    for row in df.to_dicts():
        rec = {}
        rec["Name"] = row.get(name_col, "")
        rec["Category"] = row.get(cat_col, "") if cat_col else "Uncategorized"
        rec["Description"] = html.escape(row.get(desc_col, ""))
        # Prefer paper link for name hyperlink; otherwise Source
        link = row.get(paper_col, "") if paper_col and row.get(paper_col) else row.get(source_col, "")
        if link:
            rec["Name"] = make_link(rec["Name"], link)
        else:
            rec["Name"] = html.escape(rec["Name"]) or ""
        # Source column rendered as link if url-like
        src = row.get(source_col, "")
        rec["Source"] = make_link(src, src) if src else ""
        # store raw urls for optional validation/metadata fetching
        rec["_source_url"] = src if is_url_like(src) else ""
        rec["_paper_url"] = link if is_url_like(link) else ""
        paper_raw = row.get(paper_col, "") if paper_col else ""
        rec["_paper_raw"] = paper_raw or ""
        # Add the Paper link column into the table as 'License' (linked when URL-like)
        if paper_raw and is_url_like(paper_raw):
            rec["License"] = make_link(paper_raw, paper_raw)
        else:
            rec["License"] = html.escape(paper_raw or "")
        rec["Availability"] = row.get(avail_col, "") or ""
        rec["Tags"] = html.escape(row.get(tags_col, "") or "")
        records.append(rec)

    # Group by category
    groups = {}
    for r in records:
        cat = r.get("Category") or "Uncategorized"
        groups.setdefault(cat, []).append(r)

    # Build README content
    # Optionally validate URLs and fetch metadata (refactored into enrich_urls)
    enrich_urls(records, validate=args.validate_urls, fetch=args.fetch_metadata, workers=args.workers)

    readme_lines = [f"<style>\n{TABLE_CSS}\n</style>"]
    readme_lines.append("# Awesome Food Allergy Datasets \n")
    readme_lines.append("> A curated list of datasets, databases, and resources for food allergy research, allergen identification, drug development, and clinical applications.\n")
    # legend showing meaning of row colors
    readme_lines.append(render_legend())

    # Sort categories alphabetically, but keep 'Uncategorized' last
    cats = sorted([c for c in groups.keys() if c and c != "Uncategorized"]) + (["Uncategorized"] if "Uncategorized" in groups else [])

    for cat in cats:
        readme_lines.append(f"## {cat}\n")
        cols = [("Name", "Name"), ("Description", "Description"), ("Source", "Source"), ("License", "License"), ("Tags", "Tags")]
        table_html = render_table(groups[cat], cols)
        readme_lines.append(table_html)

    out = "\n".join(readme_lines)
    (root / "README.md").write_text(out, encoding="utf8")

    end_time = time.time()
    print(f"Preprocessing and README generation completed in {end_time - start_time:.2f} seconds. Wrote {len(groups)} category sections.")

if __name__ == "__main__":
    main()