import app.validation_helper.user_regex as user_regex
import app.validation_helper.profile_regex as profile_regex
from wtforms.validators import ValidationError
import re

def match_regex_string(regex_description, expression):
    def wrapper(form, field):
        value = field.data
        if not re.match(expression, value):
            raise ValidationError(regex_description)
    return wrapper
