from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class ThoughtForm(FlaskForm):
    automatic_thought = StringField('Thoughts', validators=[DataRequired()])
    cognitive_distortions = SelectMultipleField('Cognitive Distorions', choices=[("all-or-nothing-thinking", "All-or-Nothing Thinking"), ("overgeneralisation","Overgeneralisation"), ("mental-filter", "Mental Filter"), ("disqualifying-the-positive","Disqualifying the Positive"), ("jumping-to-conclusions","Jumping to Conclusions"), ("magnification-or-minimization","Magnification or Minimization"), ("emotional-reasoning","Emotional Reasoning"), ("should-statements","Should Statements"), ("labelling-and-mislabelling","Labelling and Mislabeling"), ("personalization","Personalization")])
    rational_response = TextAreaField('Rational Response', validators=[DataRequired()])
    submit = SubmitField('Post')
