from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import BurnsDepressionTest
from flaskblog.burns_depression_test.forms import BurnsDepressionTestForm

burns_depression_test = Blueprint('burns_depression_test', __name__)


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

labels = {
    "Thoughts and Feelings": range(0, 10),
    "Activities and Personal Relationships": range(10, 17),
    "Physical Symptoms": range(17, 22),
    "Sucidal Urges": range(22, 25)
}


answer_options = {'Not At All': 0, 'Somewhat': 1,
                      'Moderately': 2, 'A Lot': 3, 'Extremely': 4}

def level_of_depression_function(score):
    if score < 0:
        return "Error score below 0 impossible."
    if score <= 5:
        return "no depression"
    if score <= 10:
        return "normal but unhappy"
    if score <= 25:
        return "mild depression"
    if score <= 50:
        return "moderate depression"
    if score <= 75:
        return "severe depression"
    if score <= 100:
        return "extreme depression"
    if score > 100:
        return "Error score above 100 impossible."

@burns_depression_test.route("/burns_depression_test", methods=['GET', 'POST'])
@login_required
def burns_depression_test_entry():
    form = BurnsDepressionTestForm()
    if form.validate_on_submit():
        score = sum([form.q0.data, form.q1.data, form.q2.data, form.q3.data, form.q4.data, form.q5.data, form.q6.data, form.q7.data, form.q8.data, form.q9.data, form.q10.data, form.q11.data, form.q12.data, form.q13.data, form.q14.data, form.q15.data, form.q16.data, form.q17.data, form.q18.data, form.q19.data, form.q20.data, form.q21.data, form.q22.data, form.q23.data, form.q24.data])
        level_of_depression = level_of_depression_function(score)
        suicidal_concern = sum([form.q22.data, form.q23.data, form.q24.data]) > 1
        health_concern = form.q21.data > 1
        entry = BurnsDepressionTest(author=current_user, score=score, level_of_depression=level_of_depression, question_0=int(form.q0.data), question_1=int(form.q1.data), question_2=int(form.q2.data), question_3=int(form.q3.data), question_4=int(form.q4.data), question_5=int(form.q5.data), question_6=int(form.q6.data), question_7=int(form.q7.data), question_8=int(form.q8.data), question_9=int(form.q9.data), question_10=int(form.q10.data), question_11=int(form.q11.data), question_12=int(form.q12.data), question_13=int(form.q13.data), question_14=int(form.q14.data), question_15=int(form.q15.data), question_16=int(form.q16.data), question_17=int(form.q17.data), question_18=int(form.q18.data), question_19=int(form.q19.data), question_20=int(form.q20.data), question_21=int(form.q21.data), question_22=int(form.q22.data), question_23=int(form.q23.data), question_24=int(form.q24.data))
        db.session.add(entry)
        db.session.commit()
        flash('Your entry has been saved!', 'success')
        return render_template('burns_depression_results.html', score=score, level_of_depression=level_of_depression, suicidal_concern=suicidal_concern, health_concern=health_concern)

    return render_template('burns_depression_test.html', form=form, questions=questions, options=answer_options.keys())


@burns_depression_test.route('/burns_depression_test/results', methods=['POST'])
@login_required
def results():

    score = 0
    for i in range(25):
        score += answer_options[request.form[questions[i]]]
    level = level_of_depression(score)

    if answer_options[request.form[questions[22]]] + answer_options[request.form[questions[23]]] + answer_options[request.form[questions[24]]] > 1:
        suicidal_concern = True
    else:
        suicidal_concern = False

    if answer_options[request.form[questions[21]]] > 1:
        health_concern = True
    else:
        health_concern = False

    return render_template('burns_depression_results.html', title='Results', score=score, level_of_depression=level, suicidal_concern=suicidal_concern, health_concern=health_concern)


# @posts.route("/post/<int:post_id>")
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', title=post.title, post=post)


# @posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='Update Post',
#                            form=form, legend='Update Post')


# @posts.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', 'success')
#     return redirect(url_for('main.home'))
