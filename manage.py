# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in PostgreSQL using SQLAlchemy and Flask. Want to learn python and familiarize myself
with the concept of object-oriented programming. So mostly an exercise up until now. Based on
following tutorials:
- https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- https://hackersandslackers.com/demystifying-flask-application-factory/
"""

from cntct import create_app
from flask_migrate import MigrateCommand, Manager

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)