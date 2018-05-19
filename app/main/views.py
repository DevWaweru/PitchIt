from flask import render_template, request, redirect, url_for
from . import main
from ..models import User, Category, Pitch
from flask_login import login_required, current_user
from .. import db
from .forms import PitchForm, CategoryForm

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

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    category_form = CategoryForm()
    pitch_form = PitchForm()

    if category_form.validate_on_submit():
        category = category_form.category.data
        new_category = Category(categ = category)
        new_category.save_category()

        return redirect(url_for('main.home'))
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data
        print(cat)

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Home | One Minute Pitch'    
    return render_template('home.html', title = title, category_form = category_form, pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>')
@login_required
def pitch(id):
    
    my_pitch = Pitch.query.get(id)
    # final_pitch = my_pitch.pitch_content

    return render_template('pitch.html',pitch = my_pitch)
    
# @main.route('/home/pitch/new', methods = ['GET', 'POST'])
# @login_required
# def new_pitch():
#     category_form = CategoryForm()
#     pitch_form = PitchForm()

#     if category_form.validate_on_submit() and pitch_form.validate_on_submit():
#         category = category_form.category.data
#         new_category = Category(categ = category)
#         new_category.save_category()

#         pitch = pitch_form.pitch.data
#         new_pitch = Pitch(pitch_content=pitch)
#         new_pitch.save_pitch()

#         return redirect(url_for('main.home'))

