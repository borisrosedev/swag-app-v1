from .app import create_flask_app
from .db import db
import os 


def create_app():

    app = create_flask_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///swag.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")

    db.init_app(app)

    with app.app_context():
        from .db.models import User
        from .db.models import Product
        db.create_all()

    return app
