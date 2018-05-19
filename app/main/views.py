from flask import render_template, request, redirect, url_for
from . import main
from ..models import User
from flask_login import login_required, current_user
from .. import db

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    title = "Home | One Minute Pitch"

    return render_template("index.html", title=title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)