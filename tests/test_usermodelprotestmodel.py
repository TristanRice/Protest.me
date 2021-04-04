import pytest
from app.models import User, Protest
import datetime


USER_CREDENTIALS = {
    "email": "tristan@colmderis.com",
    "password": "my_password"
}

PROTEST_CONFIG = {
    "title": "title",
    "date_happening": datetime.datetime.utcnow()
}

u = User(**USER_CREDENTIALS)
p = Protest(**PROTEST_CONFIG)
u.start_protest(p)

def test_userprotest1_method1():
    assert bool(len(u.protests)), "Could not add the protest"

def test_userprotest1_method2():
    protest = u.protests[0]
    assert protest.title == PROTEST_CONFIG["title"]