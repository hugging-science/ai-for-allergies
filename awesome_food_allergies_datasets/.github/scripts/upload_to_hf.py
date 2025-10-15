#!/usr/bin/env python3
"""Upload a local folder to a Hugging Face dataset repo.

This script reads environment variable for:
 - HF_TOKEN (required)

It uses the huggingface_hub Python client to upload the folder contents.
"""
from huggingface_hub import HfApi
import os, sys
from pathlib import Path


def main():
    # Read configuration strictly from environment variables
    token = os.getenv('HF_TOKEN')
    repo_id = 'abanand34/test-dataset-ai-allergies'
    dataset_file = Path('README.md')

    if not token:
        print('INFO: HF_TOKEN not provided in environment, skipping upload')
        return 0

    if not dataset_file.exists():
        print(f'ERROR: dataset file does not exist: {dataset_file}', file=sys.stderr)
        return 3

    try:
        api = HfApi(token=token)
    except Exception as e:
        print(f'ERROR: failed to login to Hugging Face: {e}', file=sys.stderr)
        return 4

    print(f'Uploading dataset file {dataset_file} to {repo_id} as dataset...')
    try:
        api.upload_file(path_or_fileobj=dataset_file, repo_id=repo_id, repo_type='dataset', path_in_repo=dataset_file.parent.name + '/' + dataset_file.name)
    except Exception as e:
        print(f'ERROR: upload failed: {e}', file=sys.stderr)
        return 5

    print('Upload completed successfully')
    return 0

if __name__ == '__main__':
    sys.exit(main())
