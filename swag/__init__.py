from .app import create_flask_app
from .db import db

def create_app(): 
    app = create_flask_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///swag.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

    db.init_app(app)

    with app.app_context():
        from .db.models import User
        from .db.models import Product
        db.create_all()

    return app
