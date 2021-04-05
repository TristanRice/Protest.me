from app.protests.forms import CreateProtestForm
from app.models import Protest, User
from flask import flash, render_template, redirect, url_for
from flask_login import current_user
from app import db
from sqlalchemy.sql.expression import func as sqlalchemy_func
from flask import Blueprint


bp = Blueprint("protest", __name__, template_folder="templates")


# Url Prefix for these routes is /protest

# /protest/create

@bp.route("/create", methods=["POST", "GET"])
def create():
    form = CreateProtestForm()
    title, text, date = form.title.data, form.text.data, form.date.data
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    if not form.validate_on_submit():
        return render_template("create_protest.html", form=form)
    p = Protest(title=title, text=text, date_happening=date)
    current_user.start_protest(p)
    db.session.add(p)
    db.session.commit()
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
