# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

flask blueprint to handle all generic views and requests
"""

from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    """function to render landing page :return:"""
    return render_template('home.html')