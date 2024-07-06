#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create a writable directory for datasets
mkdir -p /opt/render/datasets

# Download the dataset to the writable directory
wget -O /opt/render/datasets/psgs_w100.tsv.pkl https://storage.googleapis.com/huggingface-nlp/datasets/wiki_dpr/psgs_w100.tsv.pkl

# Set up environment variables
export DATASET_PATH=/opt/render/datasets/psgs_w100.tsv.pkl
