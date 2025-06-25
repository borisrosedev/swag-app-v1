from .app import create_flask_app


def create_app():
    app = create_flask_app()
    return app