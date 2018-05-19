from flask import render_template, request, redirect, url_for
from . import main
from ..models import User, Category, Pitch
from flask_login import login_required, current_user
from .. import db

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | One Minute Pitch"

    return render_template("index.html", title=title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    title = f"{uname}'s Profile"
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user, title=title)

@main.route('/home')
@login_required
def home():

    title = 'Home | One Minute Pitch'
    
    return render_template('home.html', title = title)
