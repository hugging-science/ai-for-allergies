import pandas as pd
import re
from typing import List, Dict, Tuple, Optional
from collections import Counter
import os


CATEGORY_EMOJIS = {
    "Drug & Immunotherapy Development": "💊",
    "Computational Method Development": "🔬",
    "Cross-Reactivity Analysis": "🔄",
    "Allergen Identification & Prediction": "🔍",
    "Patient Management & Clinical Decision Support": "🏥",
    "Food Product Development & Safety": "🍽️"
}

CATEGORY_ANCHORS = {
    "Allergen Identification & Prediction": "allergen-identification--prediction",
    "Computational Method Development": "computational-method-development",
    "Cross-Reactivity Analysis": "cross-reactivity-analysis",
    "Drug & Immunotherapy Development": "drug--immunotherapy-development",
    "Food Product Development & Safety": "food-product-development--safety",
    "Patient Management & Clinical Decision Support": "patient-management--clinical-decision-support",
}

def parse_readme_datasets(readme_content: str) -> List[Dict]:
    """
    Parse datasets from README markdown content.
    Extracts datasets from all category sections (both TSV and manual entries).

    Args:
        readme_content: Full README content as string

    Returns:
        List of dataset dictionaries with keys: name, category, availability, etc.
    """
    datasets = []

    category_pattern = r'<!-- CATEGORY_(.+?)_START -->(.*?)<!-- CATEGORY_\1_END -->'
    category_matches = re.finditer(category_pattern, readme_content, re.DOTALL)

    for match in category_matches:
        category = match.group(1)
        section_content = match.group(2)

        dataset_pattern = r'^## (.+?)$\n(.*?)(?=^## |\Z|^---\s*$)'
        dataset_matches = re.finditer(dataset_pattern, section_content, re.MULTILINE | re.DOTALL)

        for dataset_match in dataset_matches:
            dataset_name = dataset_match.group(1).strip()
            dataset_content = dataset_match.group(2).strip()

            if any(emoji in dataset_name for emoji in CATEGORY_EMOJIS.values()):
                continue
            if re.match(r'^\*\d+ datasets?\*$', dataset_name):
                continue

            availability = "Unknown"
            avail_match = re.search(r'\*\*Availability:\*\*\s*([^|]+)', dataset_content)
            if avail_match:
                availability = avail_match.group(1).strip()
                availability = re.sub(r'^[🟢🟡]\s*', '', availability)

            datasets.append({
                'name': dataset_name,
                'category': category,
                'availability': availability,
                'content': dataset_content
            })

    return datasets

def convert_tsv_to_markdown(tsv_file: str, readme_file: str = "README.md"):
    """
    Convert TSV dataset file to markdown format and update README.md

    Args:
        tsv_file: Path to the TSV file
        readme_file: Path to the README.md file (default: README.md)
    """
    df = pd.read_csv(tsv_file, sep='\t')

    if os.path.exists(readme_file):
        update_readme_with_markers(df, readme_file)
    else:
        create_new_readme(df, readme_file)

    print(f"Successfully updated {readme_file} with {len(df)} datasets")

def calculate_stats(readme_content: str) -> Dict:
    """
    Calculate statistics from README content (parses all datasets - TSV and manual).

    Args:
        readme_content: Full README markdown content

    Returns:
        Dict with stats: total, open_source_count, open_source_percent, gated_count, categories
    """
    datasets = parse_readme_datasets(readme_content)

    total_datasets = len(datasets)

    category_counts = {}
    for dataset in datasets:
        category = dataset['category']
        category_counts[category] = category_counts.get(category, 0) + 1

    open_source_count = 0
    gated_count = 0

    for dataset in datasets:
        availability = dataset['availability'].lower()

        if 'open source' in availability:
            open_source_count += 1
        elif 'gated' in availability:
            gated_count += 1

    open_source_percent = int((open_source_count / total_datasets) * 100) if total_datasets > 0 else 0

    return {
        'total': total_datasets,
        'open_source_count': open_source_count,
        'open_source_percent': open_source_percent,
        'gated_count': gated_count,
        'categories': category_counts
    }

def generate_stats_section(stats: Dict) -> str:
    """Generate the stats section with badges and TOC"""
    stats_content = f"""# 🥜 Awesome Food Allergy Datasets

![Datasets](https://img.shields.io/badge/datasets-{stats['total']}-blue)
![Open Source](https://img.shields.io/badge/open%20source-{stats['open_source_percent']}%25-brightgreen)
![License](https://img.shields.io/badge/license-CC0-green)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

> A curated collection of datasets, databases, and computational resources for food allergy research, allergen identification, drug development, and clinical applications.

## 🎯 Mission

Food allergy affects **over 220 million people worldwide**. This repository serves as the **first comprehensive, open collection** of AI-ready datasets for food allergy research — spanning clinical trials, immunotherapy, genomics, proteomics, microbiome, and molecular data.

Our goal: Enable researchers, ML practitioners, and the scientific community to advance AI applications in:
- 🏥 **Early Detection & Risk Stratification**
- 💊 **Drug Design & Immunotherapy Development**
- 🌿 **Food Engineering & Hypoallergenic Product Development**

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| **Total Datasets** | {stats['total']} |
| **Open Source** | {stats['open_source_count']} ({stats['open_source_percent']}%) |
| **Gated** | {stats['gated_count']} |
| **Categories** | {len(stats['categories'])} |

### By Category
"""

    for category, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        emoji = CATEGORY_EMOJIS.get(category, "📁")
        stats_content += f"- {emoji} **{category}**: {count} datasets\n"

    stats_content += "\n\n## 📑 Table of Contents\n\n"

    for category, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        emoji = CATEGORY_EMOJIS.get(category, "📁")
        anchor = CATEGORY_ANCHORS.get(category, re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", category.lower())).strip('-'))
        stats_content += f"- [{emoji} {category}](#{anchor})\n"

    stats_content += "\n---\n"

    return stats_content

def generate_category_content(df: pd.DataFrame, category: str) -> str:
    """Generate markdown content for a specific category"""
    category_df = df[df['Category'] == category]
    markdown_lines = []

    emoji = CATEGORY_EMOJIS.get(category, "📁")

    anchor_id = CATEGORY_ANCHORS.get(category, re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", category.lower())).strip('-'))
    markdown_lines.append(f"\n<a id=\"{anchor_id}\"></a>")
    markdown_lines.append(f"\n# {emoji} {category}\n")

    for _, row in category_df.iterrows():
        name = row['Name'].strip()
        markdown_lines.append(f"## {name}\n")

        description = row['Description'].strip() if pd.notna(row['Description']) else "No description available"
        markdown_lines.append(f"{description}\n")

        info_parts = []

        if pd.notna(row['Task']) and row['Task'].strip():
            info_parts.append(f"**Task:** {row['Task'].strip()}")

        if pd.notna(row['Data_Type']) and row['Data_Type'].strip():
            info_parts.append(f"**Data Type:** {row['Data_Type'].strip()}")

        if pd.notna(row['Availability']) and row['Availability'].strip():
            availability = row['Availability'].strip()
            if availability.lower() == 'open source':
                availability_formatted = f"🟢 Open source"
            elif availability.lower() == 'gated':
                availability_formatted = f"🟡 Gated"
            else:
                availability_formatted = availability
            info_parts.append(f"**Availability:** {availability_formatted}")

        if pd.notna(row['Paper link']) and row['Paper link'].strip():
            paper_link = row['Paper link'].strip()
            if paper_link.startswith(('http://', 'https://')):
                info_parts.append(f"**Paper:** [Link]({paper_link})")

        if info_parts:
            markdown_lines.append(" | ".join(info_parts) + "\n")

        contact_line_parts = []

        if pd.notna(row['Source']) and row['Source'].strip():
            source = row['Source'].strip()
            contact_line_parts.append(f"**Source:** {source}")

        if pd.notna(row['Contact']) and row['Contact'].strip():
            contact = row['Contact'].strip()
            contact_line_parts.append(f"**Contact:** {contact}")

        if contact_line_parts:
            markdown_lines.append(" | ".join(contact_line_parts) + "\n")

        markdown_lines.append("---\n")

    return "\n".join(markdown_lines)

def generate_footer() -> str:
    """Generate the README footer"""
    footer = """
---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new datasets
- Updating existing entries
- Reporting issues

## 📜 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, all contributors have waived all copyright and related rights to this work.

## 🙏 Acknowledgments

Thanks to all our contributors and the research community for making these datasets available!

Built with ❤️ for the food allergy research community.

---

**Maintained by:** [AI for Food Allergies](https://github.com/ludocomito/ai-for-allergies)
"""

    return footer

def update_readme_with_markers(df: pd.DataFrame, readme_file: str):
    """
    Update existing README using markers to preserve manual edits.

    Process:
    1. Update TSV-managed sections (before TSV_END marker)
    2. Preserve manual entries (after TSV_END marker)
    3. Recalculate stats from complete README
    4. Update stats section
    """
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()

    category_order = df['Category'].value_counts().index.tolist()

    TSV_END_MARKER = "<!-- TSV_END -->"

    for category in category_order:
        category_start = f"<!-- CATEGORY_{category}_START -->"
        category_end = f"<!-- CATEGORY_{category}_END -->"

        category_content = generate_category_content(df, category)

        if category_start in content and category_end in content:
            pattern = f"{re.escape(category_start)}(.*?){re.escape(category_end)}"
            match = re.search(pattern, content, flags=re.DOTALL)

            if match:
                existing_section = match.group(1)

                if TSV_END_MARKER in existing_section:
                    manual_entries = existing_section.split(TSV_END_MARKER, 1)[1]
                else:
                    manual_entries = ""

                new_category_section = f"{category_start}\n{category_content}\n{TSV_END_MARKER}{manual_entries}{category_end}"

                pattern = f"{re.escape(category_start)}.*?{re.escape(category_end)}"
                content = re.sub(pattern, new_category_section, content, flags=re.DOTALL)
        else:
            footer_start = "---\n\n## 🤝 Contributing"
            new_category = f"\n{category_start}\n{category_content}\n{TSV_END_MARKER}\n{category_end}\n"

            if footer_start in content:
                content = content.replace(footer_start, new_category + footer_start)
            else:
                content += new_category

    stats = calculate_stats(content)

    STATS_START = "<!-- STATS_START -->"
    STATS_END = "<!-- STATS_END -->"

    stats_content = generate_stats_section(stats)

    if STATS_START in content and STATS_END in content:
        pattern = f"{re.escape(STATS_START)}.*?{re.escape(STATS_END)}"
        new_stats = f"{STATS_START}\n\n{stats_content}\n{STATS_END}"
        content = re.sub(pattern, new_stats, content, flags=re.DOTALL)
    else:
        new_stats = f"{STATS_START}\n\n{stats_content}\n{STATS_END}\n\n"
        content = new_stats + content

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(content)

def create_new_readme(df: pd.DataFrame, readme_file: str):
    """Create a new README from scratch with TSV_END markers"""
    category_order = df['Category'].value_counts().index.tolist()
    TSV_END_MARKER = "<!-- TSV_END -->"

    readme_parts = []

    STATS_START = "<!-- STATS_START -->"
    STATS_END = "<!-- STATS_END -->"
    readme_parts.append(f"{STATS_START}\n\n{STATS_END}\n")

    for category in category_order:
        category_start = f"<!-- CATEGORY_{category}_START -->"
        category_end = f"<!-- CATEGORY_{category}_END -->"
        category_content = generate_category_content(df, category)
        readme_parts.append(f"\n{category_start}\n{category_content}\n{TSV_END_MARKER}\n{category_end}\n")

    readme_parts.append(generate_footer())

    content = "\n".join(readme_parts)

    stats = calculate_stats(content)
    stats_content = generate_stats_section(stats)

    content = content.replace(
        f"{STATS_START}\n\n{STATS_END}",
        f"{STATS_START}\n\n{stats_content}\n{STATS_END}"
    )

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Main function to run the conversion"""
    tsv_file = "dataset/datasets_spreadsheet.tsv"
    readme_file = "README.md"

    try:
        convert_tsv_to_markdown(tsv_file, readme_file)
    except FileNotFoundError:
        print(f"Error: Could not find {tsv_file}")
        print("Please make sure the file path is correct.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
