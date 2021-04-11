import os
import json


with open("recaptcha-keys.json") as f:
    data = json.load(f)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = os.environ.get("SECRET_KEY") or "random-secret-key"
    
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = data["public_key"]
    RECAPTCHA_PRIVATE_KEY = data["private_key"]
    RECAPTCHA_OPTIONS = {"theme": "white"}
