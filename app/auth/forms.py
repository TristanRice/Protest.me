from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import re
from app.regex_helper import match_regex_string, regex_user_password, regex_user_username
from app.models import User

this_field_is_required = DataRequired(message="This field is required")
class LoginForm(FlaskForm):
    username_or_email = StringField("Username or email", validators=[this_field_is_required])
    password = StringField("Password", validators=[this_field_is_required])
    submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[
        this_field_is_required,
        User.email_is_unique,
        Email(message="Email must be valid")
    ])
    password = StringField("Password", validators=[
        this_field_is_required,
        match_regex_string(**regex_user_password)
    ])
    username = StringField("Username", validators=[
        this_field_is_required,
        User.username_is_unique,
        match_regex_string(**regex_user_username)
    ])
    submit = SubmitField("Sign in")
