# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

configuration classes that provide general app configuration, take sensitive variables (secret key, DB-URL)
from environment variables (with possibility to host sensitive variables in a -env file
"""

from os import getenv
from dotenv import load_dotenv #import dotenv to load secret variables from .env

load_dotenv() #call function to load variables from .env

class Config:
    """Class for configuring Flask-app at initialization"""

    # General
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = getenv('SECRET_KEY', None) #use secret key variable obtained from .env via getenv()

    # Flask-Debug Toolbar Config
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    #sqlalchemy config
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Bootstrap Configuration


class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

