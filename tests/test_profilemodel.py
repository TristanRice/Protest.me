import pytest
from app.models import Profile

def test_profilemodel1_method1():
    p = Profile()
    for key, value in p.__dict__.items():
        if key not in p.default_attributes:
            continue
        assert value == p.default_attributes[key]

def test_profilemodel1_method2():
    """
    Make sure that we can set the attributes correctly
    """
    profile_attrs = {
        "facebook_link": "aa"
    }
    p = Profile()
    p.set_attributes(profile_attrs)
    assert p.facebook_link == profile_attrs["facebook_link"]
    assert p.twitter_link == ""

def test_profilemodel1_method3():
    """
    Make sure that attributes which don't exist on the profile model 
    will not be assigned in Profile.set_attributes()
    """
    profile_attrs = {
        "attribute_that_should_not_exist": "this-won't-be-assigned"
    }
    p = Profile()
    p.set_attributes(profile_attrs)
    assert "attribute_that_should_not_exist" not in p.__dict__
