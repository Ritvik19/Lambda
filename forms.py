from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField

class URLForm(FlaskForm):
    url = StringField('URL')
    submit = SubmitField('Classify')