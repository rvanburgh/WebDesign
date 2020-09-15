from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, AnyOf

# TODO
# write out form input fields

answer_options = {'Not At All': 0, 'Somewhat': 1,
                      'Moderately': 2, 'A Lot': 3, 'Extremely': 4}

choices = ((-1, 'Please select an option'), (0, 'Not At All'), (1, 'Somewhat'), (2, 'Moderately'), (3, 'A Lot'), (4, 'Extremely'))

questions = [  # Thoughts and Feelings
    'Feeling sad or down in the dumps',
    'Feeling unhappy or blue',
    'Crying spells or tearfulness',
    'Feeling discouraged',
    'Feeling hopeless',
    'Low self-esteem',
    'Feeling worthless or inadequate',
    'Guilt or shame',
    'Criticising yourself or blaming yourself',
    'Difficulty making decisions',
    # Activities and Personal Relationships
    'Loss of interest in family, friends',
    'Loneliness',
    'Spending less time with family and friends',
    'Loss of motivation',
    'Loss of interest in work or other activities',
    'Avoiding work or other activities',
    'Loss of pleasure or satisfaction in life',
    # Physical Symptoms
    'Feeling tired',
    'Difficulty sleeping or sleeping too much',
    'Decreased or increased appetite',
    'Loss of interest in sex',
    'Worrying about your health',
    # Sucidal Urges
    'Do you have any suicidal thoughts?',
    'Would you like to end your life?',
    'Do you have a plan for harming yourself?']

class BurnsDepressionTestForm(FlaskForm):
    q0 = SelectField(questions[0], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q1 = SelectField(questions[1], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q2 = SelectField(questions[2], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q3 = SelectField(questions[3], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q4 = SelectField(questions[4], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q5 = SelectField(questions[5], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q6 = SelectField(questions[6], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q7 = SelectField(questions[7], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q8 = SelectField(questions[8], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q9 = SelectField(questions[9], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q10 = SelectField(questions[10], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q11 = SelectField(questions[11], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q12 = SelectField(questions[12], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q13 = SelectField(questions[13], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q14 = SelectField(questions[14], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q15 = SelectField(questions[15], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q16 = SelectField(questions[16], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q17 = SelectField(questions[17], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q18 = SelectField(questions[18], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q19 = SelectField(questions[19], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q20 = SelectField(questions[20], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q21 = SelectField(questions[21], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q22 = SelectField(questions[22], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q23 = SelectField(questions[23], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    q24 = SelectField(questions[24], choices=choices, coerce=int, default=None, validators=[AnyOf([0,1,2,3,4], message="Please select a value")])
    submit = SubmitField('Submit')