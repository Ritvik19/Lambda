from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField

class URLForm(FlaskForm):
    url = StringField('URL')
    submit = SubmitField('Classify')

class INSForm(FlaskForm):
    keyword = StringField('Keyword')
    submit = SubmitField('Inspyre')

class CuisineForm(FlaskForm):
    ingredients = StringField('Ingredients', render_kw={"placeholder": "ingredient1, ingredient2"})
    submit = SubmitField('Identify')

class SentimentForm(FlaskForm):
    sentence = StringField('Sentence')
    submit = SubmitField('Analyse')

class SpamForm(FlaskForm):
    sentence = StringField('Sentence')
    submit = SubmitField('Analyse')

class SimilarityForm(FlaskForm):
    sentence1  = StringField('Sentence 1')
    sentence2  = StringField('Sentence 2')
    submit = SubmitField('Analyse')
