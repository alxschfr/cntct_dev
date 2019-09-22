# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in SQLite using SQLAlchemy and Flask. Want to learn python and familiarize myself
with the concept of object-oriented programming. So mostly an exercise up until now.
"""

from os import getenv

from dotenv import load_dotenv #import dotenv to load secret variables from .env

load_dotenv() #call function to load variables from .env

class Config:
    """Class for configuring Flask-app at initialization"""

    # General
    SECRET_KEY = getenv('SECRET_KEY', None) #use secret key variable obtained from .env via getenv()

    # Flask-Debug Toolbar Config
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db\\cntct.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Bootstrap Configuration
    BOOTSTRAP_SERVE_LOCAL = True
