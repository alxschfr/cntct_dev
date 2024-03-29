# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

WTForm definition of different forms for handeling various requests througout the whole page,
for example signup, login as well as adding, updateing and deleting a contact
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    """WTForm class for the login form"""
    email = StringField('E-Mail:', validators=[DataRequired, Email])
    password = PasswordField('Password:', validators=[DataRequired])
    remember_me = BooleanField('Remember Me!')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    """WTForm class for the Signup form"""
    email = StringField('E-Mail:', validators=[DataRequired, Email])
    name = StringField('Name:', validators=[DataRequired])
    password = PasswordField('Password:', validators=[DataRequired])
    submit = SubmitField('Sign Up')

class AddContact(FlaskForm):
    """WTForm class for form for adding a contact"""
    user_id = HiddenField()
    first_name = StringField('First Name:', validators=[DataRequired])
    last_name = StringField('Last Name:', validators=[DataRequired])
    add_contact = SubmitField('Add')

class UpdateContact(FlaskForm):
    """WTForm class for form for updating a contact"""
    contact_id = HiddenField()
    old_fn = HiddenField()
    old_ln = HiddenField()
    new_fn = StringField()
    new_ln = StringField()
    update_contact = SubmitField('Update')

class DeleteContact(FlaskForm):
    """WTForm class for form form deleting a contact"""
    contact_id = HiddenField()
    delete_contact = SubmitField('Delete')
