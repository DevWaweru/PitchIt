from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    title = "Home | One Minute Pitch"

    return render_template("index.html", title=title)