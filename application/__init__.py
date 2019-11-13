from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CAUVForm.sqlite3'
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        from . import models
        from . import forms
        from .models import User

        # Create tables for our models
        db.create_all()
        admin = User.query.filter(User.username == 'admin').all()
        if len(admin) == 0:
            admin = User(username='admin', password='admin')
            db.session.add(admin)
            core_users = [
                'bcullen',
                'jadkins',
                'eclifton',
                'scoffman',
                'jrenwand',
                'csendelbach',
                'kzoeller'
            ]
            for each in core_users:
                user = User(
                    username=each,
                    password='password'
                )
                db.session.add(user)
            db.session.commit()

        return app
