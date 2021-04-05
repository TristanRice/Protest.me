from app.auth.forms import RegisterForm, LoginForm
from app.models import User
from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user
from app import db
from flask import Blueprint

bp = Blueprint("auth", __name__, template_folder="templates")

def find_user_by_username_or_email(val):
    filter_user = User.query.filter_by
    if "@" in val:
        return filter_user(email=val).first()
    return filter_user(username=val).first()

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm(meta={"csrf": False})
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    username_or_email, password = form.username_or_email.data, form.password.data
    user = find_user_by_username_or_email(username_or_email)
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
    email, username, password = form.email.data, form.username.data, form.password.data
    if User.email_is_taken(email):
        flash("Email is already taken")
        return redirect(url_for("auth.register"))
    u = User(email=email, username=username, password=password)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for("index"))
