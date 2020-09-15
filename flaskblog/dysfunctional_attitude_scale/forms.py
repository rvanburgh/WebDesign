from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import AnyOf

das_approval_questions = [
    'Criticism will obviously upset the person who receives the criticism',
    'It is best to give up my own interests in order to please other people',
    'I need other peoples approval in order to be happy',
    'If someone important to me expects me to do something then I really should do it',
    'My value as a person depends greatly on what others think of me'
]

das_love_questions = [
    'I cannot find happiness without being loved by another person',
    'If others dislike you, you are bound to be less happy',
    'If people whom I care about reject me, it means there is something wrong with me',
    'If a person I love does not love me, it means I am unlovable',
    'Being isolated from others is bound to lead to unhappiness'
]

das_achievement_questions = [
    'If I am to be worthwhile person, I must be truly outstanding in at least one major respect',
    'I must be a useful, productive, creative person or life has no purpose',
    'People who have good ideas are more worthy than those who do not',
    'If I do not do as well as other people, it means I am inferior',
    'If I fail at my work, then I am a failure as a person'
]

das_perfectionism_questions = [
    'If you can not do something well, there is little hint in doing it at all',
    'It is shameful for a person to display his weaknesses',
    'A person should try to be the best at everything he undertakes',
    'I should be upset if I make a mistake',
    'If I dont set the highest standards for myself, I am likely to end up a second-rate person'
]

das_entitlement_questions = [
    'If I strongly believe I deserve something, I have reason to expect that I should get it',
    'It is necessary to become frustrated if you find obstacles to getting what you want',
    'If I put other peoples needs before my own, they should help me when I need something from them',
    'If I am a good husband, then my spouse is bound to love me',
    'If I do nice things for someone, I can anticipate that they will respect me and treat me just as well as I treat them'
]

das_omnipotence_questions = [
    'I should assume responsibility for how people feel and behave if they are close to me',
    'If I criticise the way someone does something and they become angry or depressed, this means I have upset them',
    'To be a good, worthwhile moral person, I must try to help everyone who needs it',
    'If a child is having emotional or behavioural difficulties, this shows that the child’s parents have failed in some important respect',
    'I should be able to please everybody'
]

das_autonomy_questions = [
    'I cannot expect to control how I feel when something happens',
    'There is no point in trying to change upsetting emotions because they are a valid and inevitable part of daily living',
    'My moods are primarily created by factors that are largely beyond my control, such as the past, or body chemistry, or hormone cycles, or biorhythms, or chance, or fate',
    'My happiness is largely dependent on what happens to me',
    'People who have the marks of success (good looks, social status, wealth or fame) are bound to be happen thats those who do not'
]

questions = [*das_approval_questions, *das_love_questions, *das_achievement_questions, *
                 das_perfectionism_questions, *das_entitlement_questions, *das_omnipotence_questions, *das_autonomy_questions]

choices = ((100, 'Please select an option'),(-2, 'Agree Strongly'), (-1, 'Agree Slightly'),
                      (0, 'Neutral'), (1, 'Disagree Slightly'), (2, 'Disagree Strongly'))

class DysfunctionalAttitudeScaleForm(FlaskForm):
    q0 = SelectField(questions[0], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q1 = SelectField(questions[1], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q2 = SelectField(questions[2], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q3 = SelectField(questions[3], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q4 = SelectField(questions[4], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q5 = SelectField(questions[5], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q6 = SelectField(questions[6], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q7 = SelectField(questions[7], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q8 = SelectField(questions[8], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q9 = SelectField(questions[9], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q10 = SelectField(questions[10], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q11 = SelectField(questions[11], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q12 = SelectField(questions[12], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q13 = SelectField(questions[13], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q14 = SelectField(questions[14], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q15 = SelectField(questions[15], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q16 = SelectField(questions[16], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q17 = SelectField(questions[17], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q18 = SelectField(questions[18], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q19 = SelectField(questions[19], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q20 = SelectField(questions[20], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q21 = SelectField(questions[21], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q22 = SelectField(questions[22], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q23 = SelectField(questions[23], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q24 = SelectField(questions[24], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q25 = SelectField(questions[25], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q26 = SelectField(questions[26], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q27 = SelectField(questions[27], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q28 = SelectField(questions[28], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q29 = SelectField(questions[29], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q30 = SelectField(questions[30], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q31 = SelectField(questions[31], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q32 = SelectField(questions[32], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q33 = SelectField(questions[33], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    q34 = SelectField(questions[34], choices=choices, coerce=int, default=None, validators=[AnyOf([-2,-1,0,1,2], message="Please select a value")])
    submit = SubmitField('Submit')