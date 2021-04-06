from app.protests.forms import CreateProtestForm
from app.models import Protest, User
from flask import flash, render_template, redirect, url_for
from flask_login import current_user
from app import db
from app.helpers import user_must_be_authenticated, commit_items_to_session 
from sqlalchemy.sql.expression import func as sqlalchemy_func
from flask import Blueprint


bp = Blueprint("protest", __name__, template_folder="templates")


# Url Prefix for these routes is /protest

# /protest/create

@bp.route("/create", methods=["POST", "GET"])
@user_must_be_authenticated
def create():
    form = CreateProtestForm()
    if not form.validate_on_submit():
        return render_template("create_protest.html", form=form)
    title, text, date = form.get_attributes("title", "text", "date")
    p = Protest(title=title, text=text, date_happening=date)
    current_user.start_protest(p)
    commit_items_to_session(p)
    return redirect(url_for("protest.by_id", id=p.id))

# /protest/random
# This would create a lot of overhead in a large system

@bp.route("/random", methods=["GET"])
def random():
    random_protest = Protest.query.order_by(sqlalchemy_func.random()).first()
    return redirect(url_for("protest.by_id", id=random_protest.id))

# /protest/<id>

@bp.route("/<id>", methods=["GET"])
def by_id(id):
    protest = Protest.query.get(id)
    return render_template("protest.html", protest=protest)

#/protest/<id>/register

@bp.route("/<id>/register", methods=["GET", "POST"])
def register_by_id(id):
    return "aa"