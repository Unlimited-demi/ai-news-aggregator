from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # It's important for security purposes, replace 'your_secret_key' with a real key.

    from .routes import main
    app.register_blueprint(main)

    return app
