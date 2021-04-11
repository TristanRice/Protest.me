from app import db, random_words
import app
import datetime
import segno
from flask_sqlalchemy import BaseQuery
from dataclasses import dataclass
from sqlalchemy.ext.hybrid import hybrid_property


def create_random_pretty_id(n=5):
    return "".join(word.capitalize() for word in random_words(max_words=n))


@dataclass
class ProtestFilters:
    coordinates: list
    # _within_range is the meter value
    _within_range: int = 10000

    @property
    def within_range(self):
        return self._within_range

    @within_range.setter
    def within_range(self, value):
        # Value should be in the format of a number and then k or m
        # m is miles and k is kilometers
        regex_validate_withinrange_setter = r"^(\d+)([k|m])$"
        regex_match = re.match(regex_validate_withinrange_setter, value)
        if not regex_match:
            raise ValueError("Invalid range value")
        distance, unit = regex_match.groups()
        meters_in_unit = 1000 if unit == "k" else 1600
        self._within_range = distance * meters_in_unit

class Protest(db.Model):
    
    __tablename__ = "protest"

    id = db.Column(db.String(64), primary_key=True, default=create_random_pretty_id, unique=True)
    title = db.Column(db.String(128), index=True)
    text = db.Column(db.Text(1028))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_happening = db.Column(db.DateTime)
    qr_uri = db.Column(db.String(12000))

    protestors = db.relationship("Protestor", backref="protest")
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    def __init__(self, text, title, date_happening, id_max_words=5):
        self.id = create_random_pretty_id(n=id_max_words)
        self.date_created = datetime.datetime.utcnow()
        self.date_happening = date_happening
        self.title = title
        self.text = text

    def __repr__(self):
        return f"<Protest \"{self.title}\">"

    def _get_date_difference_between_now_and_protest_date(self):
        current_date = datetime.datetime.utcnow()
        difference =  self.date_happening - current_date
        return difference
        
    @property
    def has_expired(self):
        difference = self._get_date_difference_between_now_and_protest_date()
        return difference.days < 0

    @property
    def days_left(self):
        difference = self._get_date_difference_between_now_and_protest_date()
        print(difference)
        return difference.days

    @property
    def qr_code_data_uri(self):
        url = f"http://{app.config.get('SERVER_NAME')}/protest/{self.id}"
        return segno.make(url).svg_data_uri()

    @hybrid_property
    def number_of_protestors(self):
        return len(self.protestors)