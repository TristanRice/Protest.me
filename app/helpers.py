from flask_login import current_user
from flask import url_for, flash, redirect
from app.models import Protest
from flask_wtf import FlaskForm
from wtforms.validators import Optional
from app import db
import os
import secrets


def user_must_be_authenticated(func):
    """
    Decorator function for making sure a user is authenticated before being
    able to load a particular route
    """
    def _(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("You must login to view that page")
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    # Make sure that the function registered has the correct name
    _.__name__ = func.__name__
    return _

def commit_items_to_session(*args):
    for arg in args:
        db.session.add(arg)
    db.session.commit()


class FlaskFormMixin(FlaskForm):
    def __init__(self, recaptcha=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not recaptcha:
            return
        environment = os.environ.get("FLASK_ENV")
        if environment in ("development", "testing") and hasattr(self, "recaptcha"):
           self.recaptcha.validators.append(Optional())

    def get_attributes(self, *args):
        return [getattr(self, arg).data for arg in args]


def make_unique_cookie(length=64):
    return secrets.token_hex(length)

class VerifyProtestExistence:
    def __init__(self, message="That protest doesn't exist"):
        self.message = message
            
    def __call__(self, f):
        def wrapper(id, *args, **kwargs):
            p = Protest.query.get(id)
            if p:
                return f(p, *args, **kwargs)
            flash(self.message)
            return redirect(url_for("index"))
        wrapper.__name__ = f.__name__
        return wrapper
