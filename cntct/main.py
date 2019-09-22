from flask import request, render_template, redirect, Blueprint
from flask_login import login_required, current_user
from .models import Contact, db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')