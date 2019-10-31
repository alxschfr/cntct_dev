# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

make database migration command from extension flask_migrate available
"""

from cntct import create_app
from flask_migrate import MigrateCommand, Manager

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)