from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import DysfunctionalAttitudeScale
from flaskblog.dysfunctional_attitude_scale.forms import DysfunctionalAttitudeScaleForm

dysfunctional_attitude_scale = Blueprint('dysfunctional_attitude_scale', __name__)

@dysfunctional_attitude_scale.route("/dysfunctional_attitude_scale", methods=['GET', 'POST'])
@login_required
def dysfunctional_attitude_scale_entry():
    form = DysfunctionalAttitudeScaleForm()
    if form.validate_on_submit():
        approval_score = sum([form.q0.data, form.q1.data, form.q2.data, form.q3.data, form.q4.data])
        love_score = sum([form.q5.data, form.q6.data, form.q7.data, form.q8.data, form.q9.data])
        achievement_score = sum([form.q10.data, form.q11.data, form.q12.data, form.q13.data, form.q14.data])
        perfectionism_score = sum([form.q15.data, form.q16.data, form.q17.data, form.q18.data, form.q19.data])
        entitlement_score = sum([form.q20.data, form.q21.data, form.q22.data, form.q23.data, form.q24.data])
        omnipotence_score = sum([form.q25.data, form.q26.data, form.q27.data, form.q28.data, form.q29.data])
        autonomy_score = sum([form.q30.data, form.q31.data, form.q32.data, form.q33.data, form.q34.data])
        

        entry = DysfunctionalAttitudeScale(author=current_user, approval_score=approval_score, love_score=love_score, achievement_score=achievement_score, perfectionism_score=perfectionism_score, entitlement_score=entitlement_score, omnipotence_score=omnipotence_score, autonomy_score=autonomy_score, question_0=int(form.q0.data), question_1=int(form.q1.data), question_2=int(form.q2.data), question_3=int(form.q3.data), question_4=int(form.q4.data), question_5=int(form.q5.data), question_6=int(form.q6.data), question_7=int(form.q7.data), question_8=int(form.q8.data), question_9=int(form.q9.data), question_10=int(form.q10.data), question_11=int(form.q11.data), question_12=int(form.q12.data), question_13=int(form.q13.data), question_14=int(form.q14.data), question_15=int(form.q15.data), question_16=int(form.q16.data), question_17=int(form.q17.data), question_18=int(form.q18.data), question_19=int(form.q19.data), question_20=int(form.q20.data), question_21=int(form.q21.data), question_22=int(form.q22.data), question_23=int(form.q23.data), question_24=int(form.q24.data), question_25=int(form.q25.data), question_26=int(form.q26.data), question_27=int(form.q27.data), question_28=int(form.q28.data), question_29=int(form.q29.data), question_30=int(form.q30.data), question_31=int(form.q31.data), question_32=int(form.q32.data), question_33=int(form.q33.data), question_34=int(form.q34.data))
        db.session.add(entry)
        db.session.commit()
        flash('Your result has been saved!', 'success')
        return render_template('dysfunctional_attitude_scale_results.html', approval_score=approval_score, love_score=love_score, achievement_score=achievement_score, perfectionism_score=perfectionism_score, entitlement_score=entitlement_score, omnipotence_score=omnipotence_score, autonomy_score=autonomy_score)

    return render_template('dysfunctional_attitude_scale.html', form=form)


@dysfunctional_attitude_scale.route('/dysfunctional_attitude_scale/results', methods=['GET'])
@login_required
def results():
     return render_template('dysfunctional_attitude_scale_results.html', approval_score=approval_score, love_score=love_score, achievement_score=achievement_score, perfectionism_score=perfectionism_score, entitlement_score=entitlement_score, omnipotence_score=omnipotence_score, autonomy_score=autonomy_score)


@dysfunctional_attitude_scale.route('/dysfunctional_attitude_scale/history', methods=['GET'])
@login_required
def history():
    previous_results = DysfunctionalAttitudeScale.query.filter_by(author=current_user).order_by(DysfunctionalAttitudeScale.date_created.desc())
    if not previous_results:
        return EOFError
    return render_template('dysfunctional_attitude_scale_history.html', previous_results=previous_results)
