from app import db, random_words, login
from flask_login import UserMixin
from app.models.profile import Profile
import bcrypt
import hashlib
import base64
import datetime
from wtforms.validators import ValidationError


class User(UserMixin, db.Model):
    
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(128))
    username = db.Column(db.String(32))
    _password = db.Column("password", db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    protests = db.relationship("Protest", backref="users")
    profile = db.relationship("Profile", backref="users", uselist=False)

    def __init__(self, email, password, username=""):
        self.email = email
        self.password = password
        self.username = username
        self.profile = Profile()

    def _password_to_sha256_base64(self, plaintext_password):
        # Bcrypt max password length is 72, so I convert it to base64 sha256
        # hashed value to avoid this problem.
        plaintext_password = str(plaintext_password).encode()
        sha256_password = base64.b64encode(
            hashlib.sha256(plaintext_password).digest()
        )
        return sha256_password

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, plaintext_password):
        sha256_hashed = self._password_to_sha256_base64(plaintext_password)
        hashed_password = bcrypt.hashpw(sha256_hashed, bcrypt.gensalt())
        self._password = hashed_password

    def verify_password(self, plaintext_password_attempt):
        sha256_hashed = self._password_to_sha256_base64(plaintext_password_attempt)
        return bcrypt.checkpw(sha256_hashed, self.password)

    def start_protest(self, protest):
        self.protests.append(protest)

    @staticmethod
    def email_is_taken(email_attempt):
        u = User.query.filter_by(email=email_attempt).first()
        return u is not None

    def email_is_unique(form, field, message=""):
        email_attempt = field.data
        default_message = "That email is already taken"
        u = User.query.filter_by(email=email_attempt).first()
        if u is not None:
            raise ValidationError(message or default_message)

    @staticmethod
    def username_is_unique(form, field, message=""):
        username_attempt = field.data
        default_message = "Username is not unique"
        u = User.query.filter_by(username=username_attempt).first()
        if u is not None:
            raise ValidationError(message or default_message)

    def __repr__(self):
        return f"<User {self.email}>"

@login.user_loader
def load_user(id):
    return User.query.get(id)
