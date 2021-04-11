from flask import Flask, request, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.randomwords import WordRandomizer
from flask_login import LoginManager
import secrets

# Configure and create app

app = Flask(__name__, static_folder="static", static_url_path="")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
random_words = WordRandomizer()
login = LoginManager(app)

# Register blueprints

from app.auth import auth_blueprint
from app.protests import protest_blueprint
from app.user import user_blueprint
from app.profile import profile_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(protest_blueprint, url_prefix="/protest")
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(profile_blueprint, url_prefix="/profile")

def make_unique_cookie_string(length=64):
    return secrets.token_hex(length)

@app.after_request
def unique_cookie_validator(response):
    if "unique_protestor" not in request.cookies:
        seconds_in_a_year = 31_536_000 # Have the cookie last a year
        random_string = make_unique_cookie_string()
        response.set_cookie(
            key="unique_protestor", 
            value=random_string,
            max_age=seconds_in_a_year
        )
    return response

from app import models
from app.models import Protest, Protestor
from sqlalchemy import func

@app.route("/", methods=["GET"])
def index():
    relevant_protests = db.session.query(
        Protest, func.count(Protestor.protest_id).label("number_of_protestors")
    ).join(Protestor).group_by(Protest).order_by(db.text("number_of_protestors DESC")).limit(10).all()
    print(relevant_protests)
    return render_template("index.html", protests=relevant_protests)

print(app.url_map)
