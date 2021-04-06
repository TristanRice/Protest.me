from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from app.validation_helper import match_regex_string, profile_regex
from wtforms.validators import Optional

class UpdateProfileForm(FlaskForm):
    twitter_link = StringField("Twitter link", validators=[
        Optional(),
        match_regex_string(**profile_regex.twitter_link)
    ])
    youtube_link = StringField("Youtube link", validators=[
        Optional(),
        match_regex_string(**profile_regex.youtube_link)
    ])
    instagram_link = StringField("Instagram link", validators=[
        Optional(),
        match_regex_string(**profile_regex.instagram_link)
    ])
    facebook_link = StringField("Facebook link", validators=[
        Optional(),
        match_regex_string(**profile_regex.facebook_link)
    ])
    submit = SubmitField("Submit form")
