#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Download the dataset
mkdir -p /var/app/datasets
wget -O /var/app/datasets/psgs_w100.tsv.pkl https://storage.googleapis.com/huggingface-nlp/datasets/wiki_dpr/psgs_w100.tsv.pkl

# Set up environment variables (if needed)
export DATASET_PATH=/var/app/datasets/psgs_w100.tsv.pkl
