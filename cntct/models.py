# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask.

definition of database model classes for SQLAlchemy's object relational mapping (ORM). Currently
one model for the representation of a user and one model for a contact entry.
"""
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    """
    model to represent a single user with id as primary key,
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    contacts = db.relationship("Contact")

    def __repr__(self):
        """
        string representation function for user objects
        :return:
        """
        return 'ID: {}, E-Mail: {}, Password: {}, Name: {}'.format(self.id, self.email,
                                                                   self.password, self.name)

class Contact(db.Model):
    """
    model to represent a single contact in the database with contact_id as primary key and two
    variables for storing information (first_name, last_name)
    """
    __tablename__ = 'contacts'
    contact_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # TODO: add more contact related objects

    def __repr__(self):
        """
        string representation function for contact objects
        :return:
        """
        return 'ID: {}, First Name: {}, Last Name: {}'.format(self.contact_id,
                                                              self.first_name, self.last_name)
