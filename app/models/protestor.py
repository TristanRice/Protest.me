from app import db
from datetime import datetime


class Protestor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    cookie_unique = db.Column(db.String(128))

    protest_id = db.Column("protest_id", db.Integer, db.ForeignKey("protest.id"))
    
    @staticmethod
    def is_unique(cookie_unique, protest_id):
        p = Protestor.query.filter_by(
            cookie_unique=cookie_unique,
            protest_id=protest_id
        ).first()
        return not p