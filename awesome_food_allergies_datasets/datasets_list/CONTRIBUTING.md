Thank you for your interest in contributing datasets to the "Awesome Food Allergy Datasets" collection!

This document explains what to include for a dataset entry and the recommended workflow for adding datasets to the repository.

What to include
---------------
Please provide the following information for each dataset entry. Using the TSV template below will make pull requests easier to review.

- Name: Official dataset or resource name
- Category: One of the high-level categories used in the repo (e.g., "Drug & Immunotherapy Development", "Cross-Reactivity Analysis", "Food Product Development & Safety", "Patient Management & Clinical Decision Support", "Computational Method Development", "Food & Ingredient Data", etc.)
- Description: One or two sentences describing what the dataset contains and its intended use
- Task / Tags: Short list of tasks or tags (comma-separated) such as "Drug Design, Target Interaction, Allergenicity Assessment"
- Data_Type: The type of data (e.g., Clinical, Molecular, Chemical, Omics, Mixed, Food)
- Source: A short label and/or URL where the dataset can be downloaded or accessed
- Paper link: (optional) A DOI, PubMed, arXiv or other reference URL
- Availability: One of "Open source", "Gated" (this controls the Access column shown in generated Markdown)
- Contact: (optional) an email or contact instructions when applicable

New workflow: generating README sections
-------------------------------------
We provide a small, simple generator that converts `datasets_spreadsheet.tsv` into a Markdown file and a synchronizer that inserts those generated sections into the `README.md` safely.

1. Generate the per-category Markdown (does not modify README):

	```powershell
	python .\awesome_food_allergies_datasets\datasets_list\generate_markdown_tables.py --tsv .\datasets_spreadsheet.tsv --output .\DATASETS_BY_CATEGORY.md
	```

	This produces `DATASETS_BY_CATEGORY.md` containing one `## Category` section per category and tables with columns: Name, Description, Source, License, Tags, Access.

2. Sync selected or all sections into `README.md` between markers. The synchronizer will back up your README to `README.md.bak` before editing.

	- To sync all generated sections:

	  ```powershell
	  python .\awesome_food_allergies_datasets\datasets_list\sync_datasets_to_readme.py --source .\DATASETS_BY_CATEGORY.md --readme .\README.md
	  ```

	- To sync only a subset of categories (comma-separated, case-insensitive):

	  ```powershell
	  python .\awesome_food_allergies_datasets\datasets_list\sync_datasets_to_readme.py --categories "Drug & Immunotherapy Development, Clinical"
	  ```

	The synchronizer looks for these markers in `README.md` and replaces the content between them:

	<!-- DATASETS_START -->
	<!-- DATASETS_END -->

	If the markers are missing the script will append them and add the generated content at the end of the file.

How to propose
---------------
Option A — Pull Request (recommended):
1. Fork the repository and create a branch in your fork.
2. Add the dataset to `datasets_spreadsheet.tsv` as a new row, following the existing TSV column order.
3. Run `generate_markdown_tables.py` locally to produce `DATASETS_BY_CATEGORY.md` and optionally inspect it.
4. Use the synchronizer to inject selected or all categories into `README.md` if you want to include the generated sections in your PR (the script creates a `README.md.bak` backup):

	```powershell
	python .\awesome_food_allergies_datasets\datasets_list\sync_datasets_to_readme.py --source .\DATASETS_BY_CATEGORY.md --readme .\README.md
	```

5. Commit the updated `datasets_spreadsheet.tsv` (and `README.md` if you regenerated/synced it) and open a pull request to `main` with a concise description.

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