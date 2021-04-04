from app import db, random_words, login
from flask_login import UserMixin
import bcrypt
import hashlib
import base64
import datetime


class User(UserMixin, db.Model):
    
    __tablename__ = "user"

    id        = db.Column(db.Integer, primary_key=True, index=True)
    email     = db.Column(db.String(128))
    _password = db.Column("password", db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    protests = db.relationship("Protest", backref="users")

    def __init__(self, email, password):
        self.email = email
        self.password = password

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

    def __repr__(self):
        return f"<User {self.email}>"

@login.user_loader
def load_user(id):
    return User.query.get(id)