
from flask import Flask
from .config import Configuration
from .models import db  # Import your database instance here
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Load configuration from Configuration class
    app.config.from_object(Configuration)

    # Initialize the database extension with the app


    # Register your blueprints or routes here, if any.

    return app
