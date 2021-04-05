from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.randomwords import WordRandomizer
from flask_login import LoginManager

# Configure and create app

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
random_words = WordRandomizer()
login = LoginManager(app)

# Register blueprints

from app.auth import auth_blueprint
from app.protests import protest_blueprint
from app.user import user_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(protest_blueprint, url_prefix="/protest")
app.register_blueprint(user_blueprint, url_prefix="/user")

print(app.url_map)

@app.route("/", methods=["GET"])
def index():
    return "index"

from app import models