from flask import Blueprint
from flask_login import current_user
from flask import flash, render_template, redirect, url_for
from app.models import User


bp = Blueprint("user", __name__, template_folder="templates")

@bp.route("/<username>", methods=["GET"])
def by_username(username):
    u = User.query.filter_by(username=username).first()
    if not u:
        return "Username not found", 404
    return render_template("user.html", user=u)
