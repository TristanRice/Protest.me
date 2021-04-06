from app.profile.forms import UpdateProfileForm
from app.models import Protest, User, Profile
from flask import flash, render_template, redirect, url_for, request
from flask_login import current_user
from app import db
from app.helpers import user_must_be_authenticated, commit_items_to_session
from flask import Blueprint


bp = Blueprint("profile", __name__, template_folder="templates")

@bp.route("/update", methods=["GET", "POST"])
@user_must_be_authenticated
def update():
    form = UpdateProfileForm()
    if not form.validate_on_submit():
        return render_template("update_profile.html", form=form)
    form_as_dict = request.form.to_dict()
    p = Profile()
    p.set_attributes(form_as_dict)
    current_user.profile = p
    commit_items_to_session(p)
    return redirect(url_for("user.by_username", username=current_user.username))
