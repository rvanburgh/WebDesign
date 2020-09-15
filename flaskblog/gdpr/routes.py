from flask import Blueprint, render_template, url_for, flash, redirect
from flaskblog.models import Thought, BurnsDepressionTest, DysfunctionalAttitudeScale, Gratitude
from flask_login import current_user, login_required
from flaskblog import db

gdpr = Blueprint('gdpr', __name__)


@gdpr.route("/gdpr", methods=['GET', 'POST'])
@login_required
def view():
    thoughts_data = Thought.query.filter_by(author=current_user).order_by(Thought.date_posted.desc())
    dysfunctional_attitude_data = DysfunctionalAttitudeScale.query.filter_by(author=current_user).order_by(DysfunctionalAttitudeScale.date_created.desc())
    burns_data = BurnsDepressionTest.query.filter_by(author=current_user).order_by(BurnsDepressionTest.date_created.desc())
    gratitude_data = Gratitude.query.filter_by(author=current_user).order_by(Gratitude.date_posted.desc())
    
    return render_template("gdpr.html", thoughts_data=thoughts_data, dysfunctional_attitude_data=dysfunctional_attitude_data, burns_data=burns_data, gratitude_data=gratitude_data)

@gdpr.route("/delete_all/", methods=['POST'])
def delete_all():
    Thought.query.filter_by(author=current_user).delete()
    DysfunctionalAttitudeScale.query.filter_by(author=current_user).delete()
    BurnsDepressionTest.query.filter_by(author=current_user).delete()
    Gratitude.query.filter_by(author=current_user).order_by(Gratitude.date_posted.desc())
    db.session.commit()
    flash('Your data has been deleted!', 'success')
    return redirect(url_for('main.home'))