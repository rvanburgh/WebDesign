from flask import render_template, request, Blueprint
from flaskblog.models import Thought, BurnsDepressionTest, DysfunctionalAttitudeScale
from flask_login import current_user, login_required
from sqlalchemy.sql import func
from flaskblog import db

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():

    cognitive_distortions_count = {
        "all_or_nothing_thinking": Thought.query.filter_by(author=current_user).filter_by(all_or_nothing_thinking=True).count(),
        "overgeneralisation": Thought.query.filter_by(author=current_user).filter_by(overgeneralisation=True).count(),
        "mental_filter": Thought.query.filter_by(author=current_user).filter_by(mental_filter=True).count(),
        "disqualifying_the_positive": Thought.query.filter_by(author=current_user).filter_by(disqualifying_the_positive=True).count(),
        "jumping_to_conclusions": Thought.query.filter_by(author=current_user).filter_by(jumping_to_conclusions=True).count(),
        "magnification_or_minimization": Thought.query.filter_by(author=current_user).filter_by(magnification_or_minimization=True).count(),
        "emotional_reasoning": Thought.query.filter_by(author=current_user).filter_by(emotional_reasoning=True).count(),
        "should_statements": Thought.query.filter_by(author=current_user).filter_by(should_statements=True).count(),
        "labelling_mislabeling": Thought.query.filter_by(author=current_user).filter_by(labelling_mislabeling=True).count(),
        "personalization": Thought.query.filter_by(author=current_user).filter_by(personalization=True).count()
    }

    mood_sum = {
        "anger" : Thought.query.with_entities(func.sum(Thought.anger)).filter_by(author=current_user).first()[0],
        "disgust" : Thought.query.with_entities(func.sum(Thought.disgust)).filter_by(author=current_user).first()[0],
        "fear" : Thought.query.with_entities(func.sum(Thought.fear)).filter_by(author=current_user).first()[0],
        "guilt" : Thought.query.with_entities(func.sum(Thought.guilt)).filter_by(author=current_user).first()[0],
        "joy" : Thought.query.with_entities(func.sum(Thought.joy)).filter_by(author=current_user).first()[0],
        "sadness" : Thought.query.with_entities(func.sum(Thought.sadness)).filter_by(author=current_user).first()[0],
        "shame" : Thought.query.with_entities(func.sum(Thought.shame)).filter_by(author=current_user).first()[0]
    }
    depression_tests = BurnsDepressionTest.query.filter_by(author=current_user)
    dysfunctional_attitudes = DysfunctionalAttitudeScale.query.filter_by(author=current_user)
    
    most_common_cognitive_distortions = 0
    most_common_emotions = 0


    page = request.args.get('page', 1, type=int)
    thoughts = Thought.query.filter_by(author=current_user).order_by(Thought.date_posted.desc()).paginate(page=page, per_page=5)
    if thoughts is not None:
        return render_template('home.html', name=current_user.name, thoughts=thoughts, cognitive_distortions_count=cognitive_distortions_count, mood_sum=mood_sum )
    else:
        return EOFError


@main.route("/about")
def about():
    return render_template('about.html', title='About')
