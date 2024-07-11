
# AI-Powered News Aggregator and Fact-Checker

## Overview
The AI-Powered News Aggregator and Fact-Checker is a web application designed to collect news articles from various sources, summarize them, and verify their credibility using natural language processing (NLP) techniques. The application leverages pre-trained models for summarization and fact-checking, providing users with concise and reliable information.

![Overview](https://via.placeholder.com/800x400.png?text=Project+Overview)

## Installation

### Prerequisites
- Python 3.9
- Docker (for containerization)
- PyTorch

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI-News-Aggregator-Fact-Checker.git
    cd AI-News-Aggregator-Fact-Checker
    ```
    
    ![Clone Repository](https://via.placeholder.com/800x400.png?text=Clone+Repository)

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    
    ![Set up Virtual Environment](https://via.placeholder.com/800x400.png?text=Set+up+Virtual+Environment)

3. **Training the Model (Optional)**:
    If you need to train or retrain the model, use the provided Colab notebook:
    1. Open the Colab notebook: [Training Notebook](link_to_your_colab_notebook)
    2. Run the cells to train the model and save the retriever and model to `.pkl` files.
    3. Download the `.pkl` files (`retriever.pkl`, `model.pkl`, `tokenizer.pkl`) and place them in the root directory of this project.
    
    ![Train Model](https://via.placeholder.com/800x400.png?text=Train+Model)

4. **Running the Application**:
    ```bash
    python run.py
    ```
    
    ![Run Application](https://via.placeholder.com/800x400.png?text=Run+Application)

5. **Using Docker**:
    1. Build the Docker image:
        ```bash
        docker build -t ai-news-aggregator-fact-checker .
        ```
        
        ![Build Docker Image](https://via.placeholder.com/800x400.png?text=Build+Docker+Image)

    2. Run the Docker container:
        ```bash
        docker run -p 8000:8000 ai-news-aggregator-fact-checker
        ```
        
        ![Run Docker Container](https://via.placeholder.com/800x400.png?text=Run+Docker+Container)

## Usage
- Access the web application at `http://127.0.0.1:8000/`
- Enter a news article URL to get a summary and fact-checking results.

![Usage](https://via.placeholder.com/800x400.png?text=Usage)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
