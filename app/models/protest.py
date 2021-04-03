from app import db, random_words
import datetime

def create_random_pretty_id(n=5):
    return "".join(word.capitalize() for word in random_words(max_words=n))

class Protest(db.Model):
    
    __tablename__ = "protests"

    id = db.Column(db.String(64), primary_key=True, default=create_random_pretty_id, unique=True)
    title = db.Column(db.String(128), index=True)
    date_created = db.Column("date_created", db.DateTime, default=datetime.datetime.utcnow)
    date_happening = db.Column("date_happening", db.DateTime)

    def __init__(self, title, date_happening, id_max_words=5):
        self.id = create_random_pretty_id(n=id_max_words)
        self.date_created = datetime.datetime.utcnow()
        self.date_happening = date_happening
        self.title = title

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