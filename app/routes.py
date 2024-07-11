from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Serve the home page."""
    return jsonify({"message": "Welcome to the News Fact-Checker API"})


from flask import request, jsonify
from .models import fetch_news

@main.route('/news')
def get_news():
    """Endpoint to get news based on user query."""
    query = request.args.get('query', '')  # Default to empty string if no query provided
    news = fetch_news(query)
    return jsonify(news)


from flask import request, jsonify
from .models import check_fact

@main.route('/fact_check', methods=['POST'])
def fact_check():
    """Endpoint to check facts."""
    data = request.get_json()
    result = check_fact(data['query'])
    return jsonify({"result": result})
