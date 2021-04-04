from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import re


def password_is_strong(form, field):
    password = field.data
    regex_description = "Password must contain eight characters, at least one letter and one number"
    regex_password_strength = "(?=.*[_!@#$%^&*-])(?=.*[0-9])(?!.*[.\n])(?=.*[a-z])(?=.*[A-Z])^.{8,}$"
    if not re.match(regex_password_strength, password):
        raise ValidationError(regex_description)

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="This field is required")])
    password = StringField("Password", validators=[DataRequired(message="This field is required")])
    submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="This field is required"),
        Email(message="Email must be valid")
    ])
    password = StringField("Password", validators=[
        DataRequired(message="This field is required"),
        password_is_strong
    ])
    submit = SubmitField("Sign in")
