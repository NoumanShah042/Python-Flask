# flaskblog/__init__.py
from flask import Flask
from flask_bcrypt import Bcrypt  # pip install Flask-Bcrypt https://pypi.org/project/Flask-Bcrypt/
from flask_sqlalchemy import SQLAlchemy  # pip install Flask-SQLAlchemy = https://pypi.org/project/Flask-SQLAlchemy/
from flask_login import LoginManager  # pip install Flask-Login = https://pypi.org/project/Flask-Login/
from flask_msearch import Search  # pip install flask-msearch = https://pypi.org/project/flask-msearch/

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flaskblog import routes