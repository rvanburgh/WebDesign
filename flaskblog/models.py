from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    thoughts = db.relationship('Thought', backref='author', lazy=True)
    burns_depression_tests = db.relationship('BurnsDepressionTest', backref='author', lazy=True)
    dysfunctional_attitude_scales = db.relationship('DysfunctionalAttitudeScale', backref='author', lazy=True)
    gratitudes = db.relationship('Gratitude', backref='author', lazy=True)
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"


class Thought(db.Model):
    __tablename__ = 'thoughts'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    automatic_thought = db.Column(db.Text, nullable=False)
    all_or_nothing_thinking = db.Column(db.Boolean)
    overgeneralisation = db.Column(db.Boolean)
    mental_filter = db.Column(db.Boolean)
    disqualifying_the_positive = db.Column(db.Boolean)
    jumping_to_conclusions = db.Column(db.Boolean)
    magnification_or_minimization = db.Column(db.Boolean)
    emotional_reasoning = db.Column(db.Boolean)
    should_statements = db.Column(db.Boolean)
    labelling_mislabeling = db.Column(db.Boolean)
    personalization = db.Column(db.Boolean)
    anger = db.Column(db.Integer)
    disgust = db.Column(db.Integer)
    fear = db.Column(db.Integer)
    guilt = db.Column(db.Integer)
    joy = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    shame = db.Column(db.Integer)
    rational_response = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Thought('{self.automatic_thought}', '{self.date_posted}')"


# TODO
# Add depression test results, dyfunctional attitude results and thought log entry
# Need to combine Post and Though log too
class BurnsDepressionTest(db.Model):
    __tablename__ = 'burns_depression_tests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=False)
    level_of_depression = db.Column(db.Integer, nullable=False)
    question_0 = db.Column(db.Integer, nullable=False)
    question_1 = db.Column(db.Integer, nullable=False)
    question_2 = db.Column(db.Integer, nullable=False)
    question_3 = db.Column(db.Integer, nullable=False)
    question_4 = db.Column(db.Integer, nullable=False)
    question_5 = db.Column(db.Integer, nullable=False)
    question_6 = db.Column(db.Integer, nullable=False)
    question_7 = db.Column(db.Integer, nullable=False)
    question_8 = db.Column(db.Integer, nullable=False)
    question_9 = db.Column(db.Integer, nullable=False)
    question_10 = db.Column(db.Integer, nullable=False)
    question_11 = db.Column(db.Integer, nullable=False)
    question_12 = db.Column(db.Integer, nullable=False)
    question_13 = db.Column(db.Integer, nullable=False)
    question_14 = db.Column(db.Integer, nullable=False)
    question_15 = db.Column(db.Integer, nullable=False)
    question_16 = db.Column(db.Integer, nullable=False)
    question_17 = db.Column(db.Integer, nullable=False)
    question_18 = db.Column(db.Integer, nullable=False)
    question_19 = db.Column(db.Integer, nullable=False)
    question_20 = db.Column(db.Integer, nullable=False)
    question_21 = db.Column(db.Integer, nullable=False)
    question_22 = db.Column(db.Integer, nullable=False)
    question_23 = db.Column(db.Integer, nullable=False)
    question_24 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"BurnsDepressionTest('{self.id}', '{self.score}', '{self.level_of_depression}')"


class DysfunctionalAttitudeScale(db.Model):
    __tablename__ = 'dysfunctional_attitude_scales'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    approval_score = db.Column(db.Integer, nullable=False)
    love_score = db.Column(db.Integer, nullable=False)
    achievement_score = db.Column(db.Integer, nullable=False)
    perfectionism_score = db.Column(db.Integer, nullable=False)
    entitlement_score = db.Column(db.Integer, nullable=False)
    omnipotence_score = db.Column(db.Integer, nullable=False)
    autonomy_score = db.Column(db.Integer, nullable=False)
    question_0 = db.Column(db.Integer, nullable=False)
    question_1 = db.Column(db.Integer, nullable=False)
    question_2 = db.Column(db.Integer, nullable=False)
    question_3 = db.Column(db.Integer, nullable=False)
    question_4 = db.Column(db.Integer, nullable=False)
    question_5 = db.Column(db.Integer, nullable=False)
    question_6 = db.Column(db.Integer, nullable=False)
    question_7 = db.Column(db.Integer, nullable=False)
    question_8 = db.Column(db.Integer, nullable=False)
    question_9 = db.Column(db.Integer, nullable=False)
    question_10 = db.Column(db.Integer, nullable=False)
    question_11 = db.Column(db.Integer, nullable=False)
    question_12 = db.Column(db.Integer, nullable=False)
    question_13 = db.Column(db.Integer, nullable=False)
    question_14 = db.Column(db.Integer, nullable=False)
    question_15 = db.Column(db.Integer, nullable=False)
    question_16 = db.Column(db.Integer, nullable=False)
    question_17 = db.Column(db.Integer, nullable=False)
    question_18 = db.Column(db.Integer, nullable=False)
    question_19 = db.Column(db.Integer, nullable=False)
    question_20 = db.Column(db.Integer, nullable=False)
    question_21 = db.Column(db.Integer, nullable=False)
    question_22 = db.Column(db.Integer, nullable=False)
    question_23 = db.Column(db.Integer, nullable=False)
    question_24 = db.Column(db.Integer, nullable=False)
    question_25 = db.Column(db.Integer, nullable=False)
    question_26 = db.Column(db.Integer, nullable=False)
    question_27 = db.Column(db.Integer, nullable=False)
    question_28 = db.Column(db.Integer, nullable=False)
    question_29 = db.Column(db.Integer, nullable=False)
    question_30 = db.Column(db.Integer, nullable=False)
    question_31 = db.Column(db.Integer, nullable=False)
    question_32 = db.Column(db.Integer, nullable=False)
    question_33 = db.Column(db.Integer, nullable=False)
    question_34 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"DysfunctionalAttitudeScale('{self.id}', '{self.date_created}')"

class Gratitude(db.Model):
    __tablename__ = 'gratitudes'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    first_gratitude = db.Column(db.Text, nullable=False)
    second_gratitude = db.Column(db.Text, nullable=False)
    third_gratitude = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Gratitude('{self.date_posted}', '{self.first_gratitude}', '{self.second_gratitude}', '{self.third_gratitude}')"
