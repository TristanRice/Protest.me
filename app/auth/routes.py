from app.auth.forms import RegisterForm, LoginForm
from app.models import User
from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user
from app import db
from flask import Blueprint

bp = Blueprint("auth", __name__, template_folder="templates")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm(meta={"csrf": False})
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    email, password = form.email.data, form.password.data
    user = User.query.filter_by(email=email).first()
    print(user)
    if not user or not user.verify_password(password):
        flash("Username or password incorrect")
        return render_template("login.html", form=form)
    login_user(user, remember=False)
    return redirect(url_for("index"))
    
@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(meta={"csrf": False})
    if not form.validate_on_submit():
        return render_template("register.html", form=form)
    email, password = form.email.data, form.password.data
    if User.email_is_taken(email):
        flash("Email is already taken")
        return redirect(url_for("auth.register"))
    u = User(email=form.email.data, password=form.password.data)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for("index"))
