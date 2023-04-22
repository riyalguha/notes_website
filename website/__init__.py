from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from website import models

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)



    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefix='/')
    app.register_blueprint(auth , url_prefix='/')




    with app.app_context():
        from .models import User, Note
        db.create_all()
        print('Database Created')
    # create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

