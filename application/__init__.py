from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uugoazwybaczwi:7c8526f5010e90bf259421da375f1be793ab5a3f8bcead490b0a02437cbca0b3@ec2-54-243-208-234.compute-1.amazonaws.com:5432/da9779rd0a0i19'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config['SECRET_KEY'] = 'blahblah'
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        from . import models
        from . import forms

        # Create tables for our models
        db.create_all()

        return app
