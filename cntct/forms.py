from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('E-Mail:', validators=[DataRequired, Email])
    password = PasswordField('Password:', validators=[DataRequired])
    remember_me = BooleanField('Remember Me!')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    email = StringField('E-Mail:', validators=[DataRequired, Email])
    name = StringField('Name:', validators=[DataRequired])
    password = PasswordField('Password:', validators=[DataRequired])
    submit = SubmitField('Sign Up')

class AddContact(FlaskForm):
    user_id = HiddenField()
    first_name = StringField('First Name:', validators=[DataRequired])
    last_name = StringField('Last Name:', validators=[DataRequired])
    submit = SubmitField('Add')
