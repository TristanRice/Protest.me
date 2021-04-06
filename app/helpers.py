from flask_login import current_user
from flask import url_for, flash, redirect
from flask_wtf import FlaskForm
from app import db


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
    def get_attributes(self, *args):
        return [getattr(self, arg).data for arg in args]