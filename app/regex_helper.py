from wtforms.validators import ValidationError
import re

def match_regex_string(regex_description, expression):
    def wrapper(form, field):
        value = field.data
        if not re.match(expression, value):
            raise ValidationError(regex_description)
    return wrapper

regex_user_password = {
    "regex_description": "Password must contain eight characters, at least one letter and one number",
    "expression": "(?=.*[_!@#$%^&*-])(?=.*[0-9])(?!.*[.\n])(?=.*[a-z])(?=.*[A-Z])^.{8,}$"
}

regex_user_username = {
    "regex_description": "Username must only contain alphanumeric characters and underscores, and be between 4 and 32 characters",
    "expression": "^[a-zA-Z0-9_]{4,32}$"
}