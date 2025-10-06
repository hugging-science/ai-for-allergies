#!/usr/bin/env python3
"""Generate simple Markdown tables from a tab-separated dataset spreadsheet.

Produces one Markdown section per Category with columns:
Name | Description | Source | License | Tags | Access

This script is intentionally small and dependency-free (uses only the stdlib).
"""
from pathlib import Path
import argparse
import csv
import html
import re


def normalize_col(headers, candidates):
    if not headers:
        return None
    lower = {h.lower(): h for h in headers}
    for c in candidates:
        if c.lower() in lower:
            return lower[c.lower()]
    return None


def is_url_like(s: str) -> bool:
    if not s:
        return False
    s = s.strip()
    return s.startswith("http://") or s.startswith("https://")


def escape_md(cell: str) -> str:
    if cell is None:
        return ""
    # Convert to str, collapse newlines and pipes which break Markdown tables
    s = str(cell)
    s = s.replace("\n", " ").replace("\r", " ")
    s = s.replace("|", "\\|")
    s = s.strip()
    return s


def format_link(text: str, url: str) -> str:
    text = escape_md(text) or escape_md(url)
    if is_url_like(url):
        return f"[{text}]({url})"
    return text


def detect_access(avail: str) -> str:
    if not avail:
        return "Unknown"
    a = avail.strip().lower()
    if "open" in a or "public" in a or "available" in a:
        return "Open source"
    if "gate" in a or "restricted" in a or "contact" in a or "request" in a:
        return "Gated"
    return avail.strip()


def read_tsv(path: Path):
    with path.open("r", encoding="utf8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        rows = list(reader)
        headers = reader.fieldnames
    return headers, rows


def build_records(rows, headers):
    name_col = normalize_col(headers, ["Name", "name"])
    cat_col = normalize_col(headers, ["Category", "Categories", "category"]) or "Category"
    desc_col = normalize_col(headers, ["Description", "description", "Summary"]) or "Description"
    source_col = normalize_col(headers, ["Source", "source", "Source URL", "Data_Type"]) or "Source"
    paper_col = normalize_col(headers, ["Paper link", "Paper Link", "paper link", "paper_link", "Link"]) or "Paper link"
    avail_col = normalize_col(headers, ["Availability", "availability"]) or "Availability"
    tags_col = normalize_col(headers, ["Tags", "Task", "task", "Tags "]) or "Tags"

    records = []
    for r in rows:
        name_raw = r.get(name_col, "") if name_col else r.get("Name", "")
        paper_raw = r.get(paper_col, "") if paper_col else ""
        src_raw = r.get(source_col, "") if source_col else ""

        # Name: link to paper when available, otherwise plain text
        if paper_raw and is_url_like(paper_raw):
            name = format_link(name_raw, paper_raw)
        else:
            name = escape_md(name_raw)

        # Description: plain escaped markdown
        desc = escape_md(r.get(desc_col, "") or "")

        # Source: if url-like, markdown link; otherwise plain text
        source = format_link(r.get(source_col, "") or "", r.get(source_col, "") or "")

        # License column: use Paper link column as License (linked when URL-like)
        license_val = r.get(paper_col, "") or ""
        license_cell = format_link(license_val, license_val) if license_val else ""

        tags = escape_md(r.get(tags_col, "") or "")
        category = r.get(cat_col, "") or "Uncategorized"
        access = detect_access(r.get(avail_col, "") or "")

        records.append({
            "Name": name,
            "Description": desc,
            "Source": source,
            "License": license_cell,
            "Tags": tags,
            "Category": category,
            "Access": access,
        })

    return records


def group_by_category(records):
    groups = {}
    for r in records:
        cat = r.get("Category") or "Uncategorized"
        groups.setdefault(cat, []).append(r)
    return groups


def render_markdown(groups, title: str = None):
    lines = []
    if title:
        lines.append(f"# {title}\n")

    cats = sorted([c for c in groups.keys() if c and c != "Uncategorized"]) + (['Uncategorized'] if 'Uncategorized' in groups else [])

    for cat in cats:
        rows = groups[cat]
        lines.append(f"## {cat}\n")
        lines.append("| Name | Description | Source | License | Tags | Access |")
        lines.append("|------|-------------|--------|---------|------|--------|")
        for r in rows:
            lines.append("| {} | {} | {} | {} | {} | {} |".format(
                r.get("Name", ""),
                r.get("Description", ""),
                r.get("Source", ""),
                r.get("License", ""),
                r.get("Tags", ""),
                r.get("Access", ""),
            ))
        lines.append("\n")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Generate Markdown tables from datasets_spreadsheet.tsv")
    p.add_argument("--tsv", help="Path to datasets TSV (tab-separated)", default="datasets_spreadsheet.tsv")
    p.add_argument("--output", help="Output Markdown file", default="DATASETS_BY_CATEGORY.md")
    p.add_argument("--title", help="Optional title for the output file", default="Datasets by Category")
    args = p.parse_args()

    tsv = Path(args.tsv)
    if not tsv.exists():
        print(f"ERROR: TSV file not found: {tsv}")
        return

    headers, rows = read_tsv(tsv)
    records = build_records(rows, headers)
    groups = group_by_category(records)
    md = render_markdown(groups, title=args.title)

    out = Path(args.output)
    out.write_text(md, encoding="utf8")
    total = sum(len(v) for v in groups.values())
    print(f"Wrote {out} with {len(groups)} categories and {total} datasets.")


if __name__ == "__main__":
    main()
