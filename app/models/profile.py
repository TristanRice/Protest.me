from app import db, random_words, login
from flask_login import UserMixin
import bcrypt
import hashlib
import base64
import datetime
from wtforms.validators import ValidationError

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    profile_picture_image_path = db.Column(db.String(64))
    description = db.Column(db.Text(1028))

    