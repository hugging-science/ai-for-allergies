#!/usr/bin/env python3
"""Sync the generated DATASETS_BY_CATEGORY.md into README.md between markers.

Usage:
  python sync_datasets_to_readme.py \ 
      --source DATASETS_BY_CATEGORY.md \ 
      --readme README.md

The script looks for markers in the README:
  <!-- DATASETS_START -->
  <!-- DATASETS_END -->

If the markers are present the content between them will be replaced. If not,
the script will append the markers and the content at the end of README.md.

The README will be backed up to README.md.bak before modification.
"""
from pathlib import Path
import argparse
import sys
import re


START_MARKER = "<!-- DATASETS_START -->"
END_MARKER = "<!-- DATASETS_END -->"


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf8")


def write_backup(path: Path) -> Path:
    bak = path.with_suffix(path.suffix + ".bak")
    bak.write_text(path.read_text(encoding="utf8"), encoding="utf8")
    return bak


def replace_between_markers(readme_text: str, new_md: str) -> str:
    if START_MARKER in readme_text and END_MARKER in readme_text:
        pre, rest = readme_text.split(START_MARKER, 1)
        _, post = rest.split(END_MARKER, 1)
        return pre + START_MARKER + "\n\n" + new_md.strip() + "\n\n" + END_MARKER + post
    else:
        # Append markers and content at the end
        if not readme_text.endswith("\n"):
            readme_text = readme_text + "\n"
        addition = f"\n{START_MARKER}\n\n{new_md.strip()}\n\n{END_MARKER}\n"
        return readme_text + addition


def parse_sections(md: str):
    """Parse markdown into ordered sections keyed by normalized '##' headings.

    Returns (ordered_keys, mapping) where mapping[normalized_title] = block_text
    including the heading line.
    """
    sections = {}
    order = []
    # find all '## Heading' occurrences
    pattern = r"(?m)^##\s+(.+?)\s*$"
    matches = list(re.finditer(pattern, md))
    if not matches:
        # no headings; treat entire md as a single unnamed section
        key = "__all__"
        sections[key] = md
        order.append(key)
        return order, sections

    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        block = md[start:end].rstrip()  # include heading
        key = re.sub(r"\s+", " ", title).strip().lower()
        sections[key] = block
        order.append(key)

    return order, sections


def replace_selected_sections(old_between: str, new_sections_map: dict, new_order: list, selected: list):
    """Replace or insert only the selected normalized headings in old_between.

    - old_between: existing content between markers (string)
    - new_sections_map: mapping normalized -> block from the generated file
    - new_order: ordered list of normalized keys from the generated file
    - selected: list of normalized keys that should be synced (if empty -> sync all)
    """
    # If no selection provided, just return new full content
    if not selected:
        # reconstruct content in new_order
        return "\n\n".join(new_sections_map[k] for k in new_order)

    # parse existing sections in the README between markers
    old_order, old_map = parse_sections(old_between)

    # Build updated list by iterating old_order and replacing any selected
    updated_parts = []
    replaced = set()
    for k in old_order:
        if k in selected and k in new_sections_map:
            updated_parts.append(new_sections_map[k])
            replaced.add(k)
        else:
            updated_parts.append(old_map.get(k, ""))

    # Append any selected sections that weren't in the old README (preserve new_order)
    for k in new_order:
        if k in selected and k not in replaced and k in new_sections_map:
            updated_parts.append(new_sections_map[k])

    return "\n\n".join(part for part in updated_parts if part)


def main():
    p = argparse.ArgumentParser(description="Sync DATASETS_BY_CATEGORY.md into README.md between markers")
    p.add_argument("--source", default="DATASETS_BY_CATEGORY.md", help="Markdown file with generated dataset tables")
    p.add_argument("--readme", default="README.md", help="Target README file to update")
    p.add_argument("--categories", default="", help="Comma-separated list of category headings to sync (case-insensitive). If omitted, all sections are synced.")
    args = p.parse_args()

    src = Path(args.source)
    readme = Path(args.readme)

    if not src.exists():
        print(f"ERROR: source file not found: {src}")
        sys.exit(2)
    if not readme.exists():
        print(f"ERROR: README file not found: {readme}")
        sys.exit(2)

    new_md = load_text(src)
    old = load_text(readme)

    # Backup
    bak = write_backup(readme)
    print(f"Backed up {readme} -> {bak}")

    # Determine the existing content between markers (if present)
    if START_MARKER in old and END_MARKER in old:
        pre, rest = old.split(START_MARKER, 1)
        between, post = rest.split(END_MARKER, 1)
    else:
        pre = old
        between = ""
        post = ""

    # Parse generated markdown into sections
    new_order, new_map = parse_sections(new_md)

    # Normalize requested categories
    selected = []
    if args.categories:
        for part in args.categories.split(','):
            key = re.sub(r"\s+", " ", part).strip().lower()
            if key:
                selected.append(key)

    updated_between = replace_selected_sections(between, new_map, new_order, selected)

    # Reconstruct full README content with markers
    updated = pre + START_MARKER + "\n\n" + updated_between.strip() + "\n\n" + END_MARKER + post

    if updated == old:
        print("No changes detected; README unchanged.")
        return

    readme.write_text(updated, encoding="utf8")
    if selected:
        print(f"Updated {readme} with selected categories: {', '.join(selected)}")
    else:
        print(f"Updated {readme} with all categories from {src} (between markers).")


if __name__ == "__main__":
    main()
