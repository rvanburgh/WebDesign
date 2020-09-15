from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import User, Thought
from flaskblog.thoughts.forms import ThoughtForm
from flaskblog.machine_learning_models.mood_detection import predict_mood

thoughts = Blueprint('thoughts', __name__)


@thoughts.route("/thought/new", methods=['GET', 'POST'])
@login_required
def new_thought():
    form = ThoughtForm()
    if form.validate_on_submit():
        all_or_nothing_thinking, overgeneralisation, mental_filter, disqualifying_the_positive, jumping_to_conclusions, magnification_or_minimization, emotional_reasoning, should_statements, labelling_mislabeling, personalization = False, False, False, False, False, False, False, False, False, False
        if "all-or-nothing-thinking" in form.cognitive_distortions.data:
            all_or_nothing_thinking = True
        if "overgeneralisation" in form.cognitive_distortions.data:
            overgeneralisation = True
        if "mental-filter" in form.cognitive_distortions.data:
            mental_filter = True
        if "disqualifying-the-positive" in form.cognitive_distortions.data:
            disqualifying_the_positive = True
        if "jumping-to-conclusions" in form.cognitive_distortions.data:
            jumping_to_conclusions = True
        if "magnification-or-minimization" in form.cognitive_distortions.data:
            magnification_or_minimization = True
        if "emotional-reasoning" in form.cognitive_distortions.data:
            emotional_reasoning = True
        if "should-statements" in form.cognitive_distortions.data:
            should_statements = True
        if "labelling-and-mislabelling" in form.cognitive_distortions.data:
            labelling_mislabeling = True
        if "personalization" in form.cognitive_distortions.data:
            personalization = True

        moods = predict_mood(form.automatic_thought.data)
        moods = {k: round(v) for k, v in moods.items()}
        # anger, disgust, fear, guilt, joy, sadness, shame = False, False, False, False, False, False, False
        # if moods['anger'] > 50:
        #     anger = True
        # if moods['disgust'] > 50:
        #     disgust = True
        # if moods['fear'] > 50:
        #     fear = True
        # if moods['guilt'] > 50:
        #     guilt = True
        # if moods['joy'] > 50:
        #     joy = True
        # if moods['sadness'] > 50:
        #     sadness = True
        # if moods['shame'] > 50:
        #     shame = True

        thought = Thought(automatic_thought=form.automatic_thought.data, all_or_nothing_thinking = all_or_nothing_thinking, overgeneralisation = overgeneralisation, mental_filter = mental_filter, disqualifying_the_positive = disqualifying_the_positive, jumping_to_conclusions = jumping_to_conclusions, magnification_or_minimization = magnification_or_minimization, emotional_reasoning = emotional_reasoning, should_statements = should_statements, labelling_mislabeling = labelling_mislabeling, personalization = personalization, rational_response = form.rational_response.data, anger=moods['anger'], disgust=moods['disgust'], fear=moods['fear'], guilt=moods['guilt'], joy=moods['joy'], sadness=moods['sadness'], shame=moods['shame'], author=current_user)
        db.session.add(thought)
        db.session.commit()
        flash('Your thought has been saved!', 'success')
        return redirect(url_for('thoughts.new_thought'))

    page = request.args.get('page', 1, type=int)
    thoughts = Thought.query.filter_by(author=current_user)\
        .order_by(Thought.date_posted.desc())\
        .paginate(page=page, per_page=5)
    # return render_template('user_thoughts.html', thoughts=thoughts, user=user)

    return render_template('create_thought.html', title='New thought',
                           form=form, thoughts=thoughts,  user=current_user, legend='New thought')


@thoughts.route("/thought/<int:thought_id>")
def thought(thought_id):
    thought = Thought.query.get_or_404(thought_id)
    if thought.author != current_user:
        abort(403)
    return render_template('thought.html', title='Thought', thought=thought)


@thoughts.route("/thought/<int:thought_id>/update", methods=['GET', 'POST'])
@login_required
def update_thought(thought_id):
    thought = Thought.query.get_or_404(thought_id)
    if thought.author != current_user:
        abort(403)
    form = ThoughtForm()
    if form.validate_on_submit():
        thought.automatic_thought = form.automatic_thought.data
        thought.rational_response = form.rational_response.data
        if "all-or-nothing-thinking" in form.cognitive_distortions.data:
            thought.all_or_nothing_thinking = True
        else:
            thought.all_or_nothing_thinking = False
        if "overgeneralisation" in form.cognitive_distortions.data:
            thought.overgeneralisation = True
        else:
            thought.overgeneralisation = False
        if "mental-filter" in form.cognitive_distortions.data:
            thought.mental_filter = True
        else:
            thought.mental_filter = False
        if "disqualifying-the-positive" in form.cognitive_distortions.data:
            thought.disqualifying_the_positive = True
        else:
            thought.disqualifying_the_positive = False
        if "jumping-to-conclusions" in form.cognitive_distortions.data:
            thought.jumping_to_conclusions = True
        else:
            thought.jumping_to_conclusions = False
        if "magnification-or-minimization" in form.cognitive_distortions.data:
            thought.magnification_or_minimization = True
        else:
            thought.magnification_or_minimization = False
        if "emotional-reasoning" in form.cognitive_distortions.data:
            thought.emotional_reasoning = True
        else:
            thought.emotional_reasoning = False
        if "should-statements" in form.cognitive_distortions.data:
            thought.should_statements = True
        else:
            thought.should_statements = False
        if "labelling-and-mislabelling" in form.cognitive_distortions.data:
            thought.labelling_mislabeling = True
        else:
            thought.labelling_mislabeling = False
        if "personalization" in form.cognitive_distortions.data:
            thought.personalization = True
        else:
            thought.personalization = False
        db.session.commit()
        flash('Your thought has been updated!', 'success')
        return redirect(url_for('thoughts.thought', thought_id=thought.id))
    elif request.method == 'GET':
        form.automatic_thought.data = thought.automatic_thought
        form.rational_response.data = thought.rational_response
        # TODO
        # Fix to autofill the form if just viewing the thought
        # form.cognitive_distortions.data = 
        page = request.args.get('page', 1, type=int)
        thoughts = Thought.query.filter_by(author=current_user)\
        .order_by(Thought.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('create_thought.html', title='Update thought',
                           form=form, thoughts=thoughts, user=current_user, legend='Update thought')


@thoughts.route("/thought/<int:thought_id>/delete", methods=['POST'])
@login_required
def delete_thought(thought_id):
    thought = Thought.query.get_or_404(thought_id)
    if thought.author != current_user:
        abort(403)
    db.session.delete(thought)
    db.session.commit()
    flash('Your thought has been deleted!', 'success')
    return redirect(url_for('main.home'))

@thoughts.route("/thought/cognitive_distortions_info", methods=['GET'])
@login_required
def cognitive_distortions_info():
    return render_template("cognitive_distortions_info.html")