Thank you for your interest in contributing datasets to the "Awesome Food Allergy Datasets" collection!

This document explains how to propose a new dataset, either by opening a pull request with a completed entry or by opening an issue to discuss before adding it.

What to include
---------------
Please provide the following information for each dataset entry. Use the template below to make a pull request easier to review.

- Name: Official dataset or resource name
- Category: One of the high-level categories used in the repo (e.g., "Drug & Immunotherapy Development", "Cross-Reactivity Analysis", "Food Product Development & Safety", "Patient Management & Clinical Decision Support", "Computational Method Development", "Food & Ingredient Data", etc.)
- Description: One or two sentences describing what the dataset contains and its intended use
- Task / Tags: Short list of tasks or tags (comma-separated) such as "Drug Design, Target Interaction, Allergenicity Assessment"
- Data_Type: The type of data (e.g., Clinical, Molecular, Chemical, Omics, Mixed, Food)
- Source: A short label and/or URL where the dataset can be downloaded or accessed
- Paper link: (optional) A DOI, PubMed, arXiv or other reference URL
- Availability: One of "Open source", "Gated", "Contact", "Private/Proprietary" (this controls row coloring)
- Contact: (optional) an email or contact instructions when applicable

How to propose
---------------
Option A — Pull Request (recommended):
1. Fork the repository and create a branch in your fork.
2. Add the dataset to `datasets_spreadsheet.tsv` as a new row, following the existing TSV column order.
3. Run `python preprocess_dataset.py` locally to regenerate `README.md` and ensure the format looks correct.
4. Commit the updated `datasets_spreadsheet.tsv` (and `README.md` if you regenerated it) and open a pull request to `main` with a concise description.

Option B — Issue (discussion first):
1. Open an issue describing the dataset and include the fields from the template above.
2. Maintainers or community members will review and suggest edits or request additional information.

Formatting tips
---------------
- Keep descriptions concise (1–3 sentences).
- Prefer canonical source URLs (project page, dataset download, or DOI) so README links are useful.

Review criteria
----------------
Maintainers will check that:
- The dataset is relevant to food allergy research or allied computational/clinical tools.
- The source is legitimate and the link resolves.
- Licensing and availability are clearly stated.

Dataset row template
--------------------
Copy this line (tab-separated) when adding to `datasets_spreadsheet.tsv`:

Name	Category	Description	Task	Data_Type	Source	Paper link	Availability	Contact

Example:
MyDataset	Drug & Immunotherapy Development	A curated set of 10,000 protein-ligand complexes for allergen-targeted drug design.	Target Interaction, Structural Analysis	Molecular	https://example.org/mydataset	https://doi.org/10.xxxx/example	Open source	

Thanks for contributing — we appreciate careful additions that improve this resource!