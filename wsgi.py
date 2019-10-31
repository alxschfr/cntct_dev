# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

WSGI-entry point to start a single app instance through flask application factory function
"""

from cntct import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
