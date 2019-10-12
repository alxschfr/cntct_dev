# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in SQLite using SQLAlchemy and Flask. Want to learn python and familiarize myself
with the concept of object-oriented programming. So mostly an exercise up until now. Based on
following tutorials:
- https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- https://hackersandslackers.com/demystifying-flask-application-factory/
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

# Globally accessible libraries (ORM for database connection and DebugToolbar
db = SQLAlchemy()
debug_tb = DebugToolbarExtension()
login_manager = LoginManager()
bs = Bootstrap()

def create_app():
    """Initialize core application with flask app factory pattern (libraries, blueprints) """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.debug = True

    # Initialise Plugins
    db.init_app(app)
    bs.init_app(app)
    debug_tb.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    with app.app_context():
        # Load User model for Login and initialize Flask-Login user_loader
        from .models import User
        @login_manager.user_loader
        def load_user(id):
            # since the user_id is just the primary key of our user table, use it in the query for the user
            return User.query.get(int(id))

        # Register blueprints for main pages, contact operations and authorization
        from .main import  main as main_bp
        app.register_blueprint(main_bp)

        from .entry import entry as entry_bp
        app.register_blueprint(entry_bp)

        from .auth import auth as auth_bp
        app.register_blueprint(auth_bp)

        # Create database tables
        db.create_all()

        return app
