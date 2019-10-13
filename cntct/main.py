# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    """function to render landing page :return:"""
    return render_template('home.html')