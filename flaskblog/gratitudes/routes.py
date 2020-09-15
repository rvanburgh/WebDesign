from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import User, Gratitude
from flaskblog.gratitudes.forms import GratitudeForm

gratitudes = Blueprint('gratitudes', __name__)


@gratitudes.route("/gratitude/new", methods=['GET', 'POST'])
@login_required
def new_gratitude():
    form = GratitudeForm()
    if form.validate_on_submit():
        gratitude = Gratitude(first_gratitude=form.first_gratitude.data, second_gratitude=form.second_gratitude.data, third_gratitude=form.third_gratitude.data, author=current_user)
        db.session.add(gratitude)
        db.session.commit()
        flash("Today's gratitude journal has been saved!", 'success')
        return redirect(url_for('gratitudes.new_gratitude'))

    page = request.args.get('page', 1, type=int)
    gratitudes = Gratitude.query.filter_by(author=current_user)\
        .order_by(Gratitude.date_posted.desc())\
        .paginate(page=page, per_page=5)
    # return render_template('user_gratitudes.html', gratitudes=gratitudes, user=user)

    return render_template('create_gratitude.html', title='Gratitude journal',
                           form=form, gratitudes=gratitudes,  user=current_user, legend='Gratitude journal')


@gratitudes.route("/gratitude/<int:gratitude_id>")
def gratitude(gratitude_id):
    gratitude = Gratitude.query.get_or_404(gratitude_id)
    if gratitude.author != current_user:
        abort(403)
    return render_template('gratitude.html', title='gratitude', gratitude=gratitude)


@gratitudes.route("/gratitude/<int:gratitude_id>/update", methods=['GET', 'POST'])
@login_required
def update_gratitude(gratitude_id):
    gratitude = Gratitude.query.get_or_404(gratitude_id)
    if gratitude.author != current_user:
        abort(403)
    form = GratitudeForm()
    if form.validate_on_submit():
        gratitude.first_gratitude = form.first_gratitude.data
        gratitude.second_gratitude = form.second_gratitude.data
        gratitude.third_gratitude = form.third_gratitude.data
        db.session.commit()
        flash('Your gratitude journal has been updated!', 'success')
        return redirect(url_for('gratitudes.gratitude', gratitude_id=gratitude.id))
    elif request.method == 'GET':
        form.first_gratitude.data = gratitude.first_gratitude
        form.second_gratitude.data = gratitude.second_gratitude
        form.third_gratitude.data = gratitude.third_gratitude
        page = request.args.get('page', 1, type=int)
        gratitudes = Gratitude.query.filter_by(author=current_user)\
        .order_by(Gratitude.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('create_gratitude.html', title='Update gratitude',
                           form=form, gratitudes=gratitudes, user=current_user, legend='Update gratitude')


@gratitudes.route("/gratitude/<int:gratitude_id>/delete", methods=['POST'])
@login_required
def delete_gratitude(gratitude_id):
    gratitude = Gratitude.query.get_or_404(gratitude_id)
    if gratitude.author != current_user:
        abort(403)
    db.session.delete(gratitude)
    db.session.commit()
    flash('Your gratitude has been deleted!', 'success')
    return redirect(url_for('gratitudes.gratitude'))
