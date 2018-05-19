from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    category = StringField('Category',validators=[Required()])
    submit = SubmitField('Submit')