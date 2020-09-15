from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class GratitudeForm(FlaskForm):
    first_gratitude = StringField("First thing you're grateful for..", validators=[DataRequired()])
    second_gratitude = StringField("Second thing you're grateful for..", validators=[DataRequired()])
    third_gratitude = StringField("Third thing you're grateful for..", validators=[DataRequired()])
    submit = SubmitField('Save')
