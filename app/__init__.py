# Init flask app, and other extensions

from flask import Flask
from .routes import main

import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from app.models import db, bcrypt, login_manager

load_dotenv()


def start_app():
    app = Flask(__name__)

    # configurate app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_URI", "sqlite:///db.sqlite3")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    Bootstrap5(app)

    # initialize db with app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    #Init bcrypt object
    bcrypt.init_app(app)

    #Init login_manager
    login_manager.init_app(app)

    # register blueprint
    app.register_blueprint(main)
    return app

