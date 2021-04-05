import pytest
from app.models import Protest, User
from app import app, db
import re
import datetime
from string import ascii_lowercase
import random
import time

test_client = app.test_client()

def create_random_username():
    return "".join(random.choice(ascii_lowercase) for _ in range(10))

def create_random_email():
    email_username = create_random_username()
    email_domain = "test.com"
    return f"{email_username}@{email_domain}"

def test_authforms1_method1():
    """
    Make sure that valid credentials are accepted
    """
    data = {
        "email": create_random_email(),
        "username": create_random_username(),
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD",
    }
    res = test_client.post("/register", data=data, follow_redirects=False)
    assert b"Redirecting..." in res.data

def test_authforms1_method2():
    """
    Make sure that invalid emails are rejected
    """
    data = {
        "email": "aaa",
        "username": "valid_username",
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    res = test_client.post("/register", data=data)
    assert b"Email must be valid" in res.data

def test_authforms1_method3():
    """
    Make sure that insecure passwords are rejected
    """
    data = {
        "email": create_random_email(),
        "username": "valid_username",
        "password": "aaa"
    }
    res = test_client.post("/register", data=data)
    assert b"Password must contain" in res.data

def test_authforms1_method4():
    """
    Make sure that duplicate emails are rejected 
    """
    email_val = create_random_email()
    data1 = {
        "email": email_val,
        "username": create_random_username(),
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    data2 = {
        "email": email_val,
        "username": create_random_username(),
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    res1 = test_client.post("/register", data=data1)
    res2 = test_client.post("/register", data=data2)
    # If the registration is successful, the user will be redirected to the index page
    assert b"<a href=\"/\">/</a>" in res1.data
    # If the registration is unsuccessful, the user will be redirected to the register page
    assert b"That email is already taken" in res2.data

def test_authforms1_method5():
    """
    Make sure that we can login users correctly
    """
    username = create_random_username()
    data_register = {
        "email": create_random_email(),
        "username": username,
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    data_login = {
        "username_or_email": username,
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    res = test_client.post("/register", data=data_register)
    assert b"<a href=\"/\">/</a>" in res.data
    test_client.delete_cookie(key="session", server_name="localhost")
    res1 = test_client.post("/login", data=data_login)
    assert b"<a href=\"/\">/</a>" in res1.data

def test_authforms1_method6():
    """
    Make sure that invalid users cannot login
    """
    data = {
        "username_or_email": "aaa",
        "password": "aaa"
    }
    # Make sure that we don't keep the login from the previous test
    test_client.delete_cookie(key="session", server_name="localhost")
    res = test_client.post("/login", data=data)
    print(res.data)
    assert b"Username or password incorrect" in res.data

def test_authforms1_method7():
    """
    Make sure that invalid usernams are rejected
    """
    data = {
        "username": "Thi$-I/s-an-invalid-username",
        "email": create_random_email(),
        "password": "Th1s-1s4-$3CuR3_P4$$W0RD"
    }
    res = test_client.post("/register", data=data)
    