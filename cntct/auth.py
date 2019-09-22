# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in SQLite using SQLAlchemy and Flask. Want to learn python and familiarize myself
with the concept of object-oriented programming. So mostly an exercise up until now.
"""

from flask import request, render_template, redirect, Blueprint, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    """function for rendering login.html"""
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    """function to process POST-request of login-route"""
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('entry.profile'))

@auth.route('/signup')
def signup():
    """funtion for rendering signup.html :return:"""
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    """function to process POSTT_request of signup-route :return:"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() #if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists! Try a different one.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    #add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    """function to logout user and redirect to landingpage :return:"""
    logout_user()
    return redirect(url_for('main.home'))