from flask import render_template, request, redirect, url_for, flash
from . import main
from ..models import User, Pitch, Comment, UpVote, DownVote
from flask_login import login_required, current_user
from .. import db
from .forms import PitchForm, CategoryForm, CommentForm

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

    title = f"{uname.capitalize()}'s Profile"
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user, title=title)

@main.route('/home/like/<int:id>', methods = ['GET','POST'])
@login_required
def like(id):
    get_pitches = UpVote.get_votes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    like_pitch = UpVote(user = current_user, pitching_id=id)
    like_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))

@main.route('/home/dislike/<int:id>', methods = ['GET','POST'])
@login_required
def dislike(id):
    get_pitches = DownVote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    dislike_pitch = DownVote(user = current_user, pitching_id=id)
    dislike_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Home | One Minute Pitch'    
    return render_template('home.html', title = title, pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):
    
    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)
    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)

    title = 'Comment | One Minute Pitch'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title, likes = up_likes, dislikes=down_likes)

@main.route('/category/<cat>')
def category(cat):
    my_category = Pitch.get_category(cat)

    title = f'{cat} category | One Minute Pitch'

    return render_template('category.html', title=title, category=my_category)