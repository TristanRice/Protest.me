import pytest
from app.models import User
import re

USER_CREDENTIALS = {
    "email": "tristan@colmderis.com", 
    "password": "my_password"
}

u = User(**USER_CREDENTIALS)

def test_user1_method1():
    """
    Make sure that we can actually create a new User object
    """
    assert u is not None, "Could not create a new User object"

def test_user1_method2():
    """
    Make sure that the values are assigned correctly
    """
    assert u.email == USER_CREDENTIALS["email"], "Email was not assigned correctly"
    assert u.password is not None, "Password was not assigned correctly"

def test_user1_method3():
    """
    Make sure that the password is hashed correctly
    """
    REGEX_MATCH_BCRYPT_HASH = r"^\$2[ayb]\$.{56}$"
    hashed_password = u.password.decode()
    assert re.match(REGEX_MATCH_BCRYPT_HASH, hashed_password), "Password was not hashed correctly"

def test_user1_method4():
    """
    Make sure that we can verify a plaintext password
    """
    assert u.verify_password(USER_CREDENTIALS["password"]), "Password cannot verify properly"