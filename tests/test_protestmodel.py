import pytest
from app.models import Protest
import re
import datetime

def create_datetime_object_n_days_from_now(days):
    today = datetime.datetime.utcnow()
    days = days - days * 2 # Convert positive -> negative and vice-versa
    # Account for the fact that the utcnow decrements a few miliseconds before the
    # tests execute
    days += -1 if days < 0 else 0
    delta = datetime.timedelta(days = days)
    return today - delta

DATE_DAYS_FROM_NOW = 5
casual_date = create_datetime_object_n_days_from_now(DATE_DAYS_FROM_NOW)

def test_protest1_method1():
    """
    Make sure that we can actually create a model
    """
    p = Protest(title="Title", date_happening=casual_date)
    assert p is not None, "Test failed because protest model could not be created"

def test_protest1_method2():
    """
    Make sure that the model attributes can be assigned correctly
    """
    TITLE_OF_PROTEST = "Title"
    regex_match_alphabetical = "^[a-zA-Z]+$"
    p = Protest(title=TITLE_OF_PROTEST, date_happening=casual_date)
    assert p.title == TITLE_OF_PROTEST, f"Test failed because protest title: ({p.title}) is not {TITLE_OF_PROTEST}"
    assert re.match(regex_match_alphabetical, p.id), "Test failed because test id is incorrect"

def test_protest1_method3():
    """
    Make sure that the dates are done correctly
    """
    p = Protest(title="Title", date_happening=casual_date)
    assert p.days_left == DATE_DAYS_FROM_NOW, "Make sure that days left is calculated correctly"
    assert not p.has_expired, "Make sure that the has_expired property is working correctly"

def test_protest1_method4():
    date_test = create_datetime_object_n_days_from_now(-5)
    p = Protest(title="Title", date_happening=date_test)
    assert p.has_expired, "Make sure that has_expired property returns true if date has expired"
    assert p.days_left == -5, "Make sure that days_left calculates negative numbers correctly"