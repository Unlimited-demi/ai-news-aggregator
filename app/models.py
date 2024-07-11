# app/models.py
import os
import requests
from datasets import load_dataset
from transformers import RagRetriever, RagTokenizer, RagTokenForGeneration

# Use the environment variable for the dataset path
dataset_path = os.getenv('DATASET_PATH', 'dataset')

# Initialize the retriever with the path to the dataset
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-nq",
    index_name="legacy",
    passages_path=dataset_path
)

# Initialize the model
model = RagTokenForGeneration.from_pretrained(
    "facebook/rag-token-nq",
    retriever=retriever
)

# Initialize the tokenizer
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")

def fetch_news(query):
    try:
        api_key = '319c238756184eb4a0f180cfbe86a293'
        base_url = "https://newsapi.org/v2/everything"
        params = {'q': query, 'apiKey': api_key}
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Will raise an exception for 4XX/5XX errors
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def check_fact(query):
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(**inputs) # type: ignore
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)
