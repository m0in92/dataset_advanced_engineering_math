"""
This document contains sample python script for loading, processing, and saving datasets.
The script uses Huggingface's dataset python package.
"""

from datasets import load_dataset, DatasetDict


dataset: DatasetDict = load_dataset(path="json",
                                    data_files="data/linear_algebra.jsonl")
print(dataset)
