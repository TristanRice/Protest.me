from app.helpers import FlaskFormMixin
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, ValidationError, Required
import re
import datetime


data_required_with_message = DataRequired(message="This field is required")

def validate_date(form, field):
    date_protest_is_happening = field.data
    date_today = datetime.datetime.utcnow().date()
    if date_today > date_protest_is_happening:
        raise ValidationError("Protest must be organized for a date later than today")
    
class CreateProtestForm(FlaskFormMixin):
    title = StringField("Title", validators=[
        data_required_with_message
    ])
    text = TextAreaField("Text", validators=[
        data_required_with_message
    ])
    date = DateField("Date happening", validators=[
        data_required_with_message,
        validate_date
    ])
    submit = SubmitField("Submit")
