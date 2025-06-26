from flask import Flask
from .routes import web
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_flask_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    CORS(app)
    app.register_blueprint(web)
    return app