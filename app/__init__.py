from flask import Flask
from .routes import web


def create_flask_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    return app