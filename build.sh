#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create a writable directory for datasets (if needed for future use)
mkdir -p /opt/render/datasets

# Set up environment variables
export DATASET_PATH=/opt/render/datasets/psgs_w100.tsv.pkl

# Download the dataset to the writable directory
if [ ! -f "$DATASET_PATH" ]; then
    wget -O "$DATASET_PATH" https://storage.googleapis.com/huggingface-nlp/datasets/wiki_dpr/psgs_w100.tsv.pkl
fi
