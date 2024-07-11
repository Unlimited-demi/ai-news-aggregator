# app/models.py
import requests
from datasets import load_dataset
from transformers import RagRetriever, RagTokenizer, RagTokenForGeneration

# Load the dataset directly from Hugging Face
dataset = load_dataset("wiki_dpr", "psgs_w100.nq.exact", split="train")

# Initialize the retriever
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-nq",
    index_name="legacy",
    use_dummy_dataset=True
)

# Manually set the passages dataset
retriever.index.dataset = dataset

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
    outputs = model.generate(**inputs)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)
