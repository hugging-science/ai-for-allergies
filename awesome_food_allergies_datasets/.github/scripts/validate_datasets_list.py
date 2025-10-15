#!/usr/bin/env python3
"""
validates datasets list in the README.md file:
checks for required fields and post a summary comment about entries not including them by category
"""

import os, re, sys, base64, requests, difflib
from typing import List, Tuple

GITHUB_API = "https://api.github.com"
required_fields = ["**Task:**", "**Data Type:**", "**Availability:**"]
optional_fields = ["**Paper:**", "**Contact:**", "**Source:**"]
availability_status_options = ["🟢 Open source", "🟡 Gated"]

data_item_format = f"""
\#\# DATASET_NAME

dataset description...

**Task:** ... | **Data Type:** ... | **Availability:** {' or '.join(f'[{opt}]' for opt in availability_status_options)} | **Paper:** [Link](paper_link)

**Source:** source_link (required for open source, optional for gated)

---



required fields (all datasets): {required_fields}
required fields (open source only): ["**Source:**"]
optional fields: {optional_fields}
"""

def die(msg): print(msg, file=sys.stderr); sys.exit(1)

def get_env(v, required=True): 
    val = os.getenv(v)
    if required and not val: die(f"Missing env: {v}")
    return val

def get_file(repo, path, ref, token):
    """
    read the file using the github API
    """

    r = requests.get(
        f"{GITHUB_API}/repos/{repo}/contents/{path}", 
        headers={
            "Authorization": f"token {token}", 
            "Accept": "application/vnd.github+json"
        },
        params={"ref": ref})

    if r.status_code == 200:
        j = r.json()
        return base64.b64decode(j["content"]).decode()

    if r.status_code == 404: return ""
    die(f"GitHub API error {r.status_code}: {r.text}")


def find_categories(readme: str):
    """
    input: the readme file text
    output: list of dataset categories listed in ## By Category
    """

    m = re.search(r"^### By Category\s*(.+?)(?=^## |\Z)", readme, flags=re.S | re.M)
    return [c.split("**")[1] for c in m.group(1).strip().splitlines()] if m else []

def extract_between(text: str, start: str, end: str) -> str:
    """
    given the reame text and tokens it extracts a dataset category
    """
    if start not in text or end not in text:
        die("Missing tokens {start} - {end}")
    m = re.search(re.escape(start) + r"(.*?)" + re.escape(end), text, flags=re.S)
    return m.group(1).strip() if m else ""

def validate_section(section: str) -> Tuple[bool, List[str]]:
    """
    given a dataset category list it checks for if each listed dataset include the expected infos:
    - task
    - data type
    - availability
    - source (required for open source, optional for gated)
    """

    failures = []
    datasets = re.findall(r"^(## .+?)$(.+?)(?=^## |\Z)", section, flags=re.S | re.M)
    for title_line, content in datasets:
        title = title_line[3:].strip()
        found_fields = re.findall(r"\*\*[^:]+:\*\*", content)

        is_gated = False
        availability_match = re.search(r'\*\*Availability:\*\*\s*([^|]+)', content)
        if availability_match:
            availability_value = availability_match.group(1).strip().lower()

            if 'gated' in availability_value or '🟡' in availability_value:
                is_gated = True

        fields_to_check = required_fields.copy()
        if not is_gated:
            fields_to_check.append("**Source:**")

        missing = [f for f in fields_to_check if f not in found_fields]
        extra = [f for f in found_fields if f not in required_fields + optional_fields]

        if missing or extra:
            failures.append({
                "dataset": title,
                "missing_fields": missing,
                "extra_fields": extra,
                "content": content
            })

    return (not failures, failures)

def post_comment(repo, pr, token, body):
    requests.post(f"{GITHUB_API}/repos/{repo}/issues/{pr}/comments",
                  headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json"},
                  json={"body": body})

def short_diff(a, b):
    d = difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="")
    return "\n".join(list(d)[:120])

def main():
    repo = get_env("REPO"); pr = int(get_env("PR_NUMBER"))
    token = get_env("GITHUB_TOKEN"); path = get_env("FILE_PATH")
    base_ref = get_env("BASE_REF"); head_ref = get_env("HEAD_REF")

    base = get_file(repo, path, base_ref, token)
    head = get_file(repo, path, head_ref, token)
    cats = find_categories(head)
    if not cats: die("No categories found (## headings missing).")

    all_valid = True
    summary = []
    for cat in cats:
        start, end = f"<!-- CATEGORY_{cat}_START -->", f"<!-- CATEGORY_{cat}_END -->"
        base_sec, head_sec = extract_between(base, start, end), extract_between(head, start, end)
        if not head_sec: die(f"Missing dataset list for a mentioned category: {cat}")
        is_valid, fails = validate_section(head_sec)
        all_valid = all_valid and is_valid
        diff = short_diff(base_sec, head_sec)
        added = len([l for l in diff.splitlines() if l.startswith("+")])
        deleted = len([l for l in diff.splitlines() if l.startswith("-")])
        if not is_valid:
            fails_summary = "\n\n\n".join([
                f"\tdataset: {entry_fail['dataset']}"\
                + ("" if not entry_fail["missing_fields"] else f" \n\tmissing fields: {', '.join(entry_fail['missing_fields'])}")
                + ("" if not entry_fail["extra_fields"] else f" \n\textra fields: {', '.join(entry_fail['extra_fields'])}")
                for entry_fail in fails
            ])
            summary.append(f"- **{cat}** → +{added}, -{deleted}, invalid: {len(fails)} \n{fails_summary}")

    if not all_valid:
        body = "### Dataset Category Validation Summary\n" + "\n".join(summary)
        body += f"\n\n\nto pass all checks make sure all added and modified dataset entries follow this format: \n{data_item_format}"
        post_comment(repo, pr, token, body)
        die("invalid data entries, details in the posted comment")

if __name__ == "__main__":
    main()