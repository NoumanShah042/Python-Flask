from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required

# We can access the logged-in user with the current_user proxy, which is available in every template:

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

login = LoginManager(app)
login.login_view = 'login'  # login function passed as string

db = SQLAlchemy(app)


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
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return '<user {}="">'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<post {}="">'.format(self.body)


@login.user_loader     #  login = LoginManager(app)
def load_user(id):
    return User.query.get(int(id))


# @login_required    will only allow user to this route if the user is login

@app.route('/')
@app.route('/index')
@login_required
def index():
    user_post = {'username': 'cairocoders'}
    hash = generate_password_hash('test1')
    check_hash = check_password_hash(hash, 'test1')
    posts = [
        {
            'author': {'username': 'tutorial1'},
            'body': 'Beautiful day in Olongapo City!'
        },
        {
            'author': {'username': 'turorial10'},
            'body': 'Flask is a lightweight WSGI web application framework.!'
        }
    ]
    return render_template('index.html', title='Home', user_post=user_post,
                           posts=posts, hash=hash, check_hash=check_hash)


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


@app.route('/rough')
@login_required
def rough():
    return f"<h1>Hello{current_user.username}</h1>"


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
