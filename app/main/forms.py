from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    my_category = StringField('Category', validators=[Required()])  
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    category = StringField('Category',validators=[Required()])
    submit = SubmitField('Submit')