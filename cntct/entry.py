# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

flask blueprint to handle all entry-related views and requests
"""

from flask import request, render_template, redirect, Blueprint
from flask_login import login_required, current_user
from .forms import AddContact, UpdateContact, DeleteContact
from .models import Contact, db

entry = Blueprint('entry', __name__)

@entry.route('/contacts', methods=['GET', 'POST'])
def contacts():
    """
    flask-function for storing input data and render the flask template for the apps main page
    :return:
    """
    add_contact = AddContact()
    update_contact = UpdateContact()
    delete_contact = DeleteContact()

    # if request.form:
    #    contact = Contact(first_name=request.form.get('first_name'),
    #                      last_name=request.form.get('last_name'),
    #                      user_id=request.form.get('user_id'))
    #    db.session.add(contact)
    #    db.session.commit()
    contacts = Contact.query.filter(Contact.user_id == current_user.id).all()
    return render_template('contacts.html', contacts=contacts, current_user=current_user,
                           add_contact=add_contact, update_contact=update_contact,
                           delete_contact=delete_contact)

@entry.route('/add', methods=['POST'])
def add():
    """
    flask-function for adding contact entries based on user input and current user id
    and committing the changes to sqlite3-database
    :return:
    """
    contact = Contact(first_name=request.form.get('first_name'),
                          last_name=request.form.get('last_name'),
                          user_id=request.form.get('user_id'))
    db.session.add(contact)
    db.session.commit()
    return redirect('/contacts')

@entry.route('/update', methods=['POST'])
def update():
    """
    flask-function for updating the existing database entries based on contact
    id and committing the changes to the sqlite3-database
    :return:
    """
    contact_id = request.form.get('contact_id')

    new_fn = request.form.get('new_fn')
    new_ln = request.form.get('new_ln')

    contact = Contact.query.filter_by(contact_id=contact_id).first()

    contact.first_name = new_fn
    contact.last_name = new_ln

    db.session.commit()
    return redirect('/contacts')

@entry.route('/delete', methods=['POST'])
def delete():
    """
    flask-function to delete specific entries from the database based on primary_key column id
    :return:
    """
    contact_id = request.form.get('contact_id')
    contact = Contact.query.filter_by(contact_id=contact_id).first()
    db.session.delete(contact)
    db.session.commit()
    return redirect('/contacts')

@entry.route('/profile')
@login_required
def profile():
    """function for rendering profile page and pass user name and user mailadress to request :return:"""
    return render_template('profile.html', name=current_user.name, email=current_user.email)

