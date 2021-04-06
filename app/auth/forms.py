from app.helpers import FlaskFormMixin
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import re
from app.validation_helper import match_regex_string, user_regex
from app.models import User

this_field_is_required = DataRequired(message="This field is required")

class LoginForm(FlaskFormMixin):
    username_or_email = StringField("Username or email", validators=[this_field_is_required])
    password = StringField("Password", validators=[this_field_is_required])
    submit = SubmitField("Sign in")
    recaptcha = RecaptchaField()

class RegisterForm(FlaskFormMixin):
    email = StringField("Email", validators=[
        this_field_is_required,
        User.email_is_unique,
        Email(message="Email must be valid")
    ])
    password = StringField("Password", validators=[
        this_field_is_required,
        match_regex_string(**user_regex.password)
    ])
    username = StringField("Username", validators=[
        this_field_is_required,
        User.username_is_unique,
        match_regex_string(**user_regex.username)
    ])
    submit = SubmitField("Sign in")
