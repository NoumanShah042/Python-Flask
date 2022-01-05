from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# ModuleNotFoundError: No module named 'flask_sqlalchemy' = (venv) C:\flaskmyproject>pip install Flask-SQLAlchemy
# ModuleNotFoundError: No module named 'flask_login' = (venv) C:\flaskmyproject>pip install flask_login
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

# import sqlite3

app = Flask(__name__)
# conn = sqlite3.connect('flask_login.db')
# print("Opened database successfully");

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_login.db'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<user {}="">'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@app.route('/')
def index():
    hash = generate_password_hash('1234')
    check_hash = check_password_hash(hash, '1234')
    return render_template('index.html', hash=hash, check_hash=check_hash)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.username


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'


if __name__ == '__main__':
    app.run(debug=True)
