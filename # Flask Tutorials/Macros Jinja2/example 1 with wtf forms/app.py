from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


app.config['SECRET_KEY'] = 'cairocoders-ednalan'


# https://www.youtube.com/watch?v=HY0le1NAczc

class RegistrationForm(FlaskForm):
    """ Registration form"""

    username = StringField('username', validators=[InputRequired(message="Username required"), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), Length(
        min=4, max=25, message="Password must be between 4 and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd', validators=[InputRequired(
        message="Password required"), EqualTo('password', message="Passwords must match")])


@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Update database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        print("username", username)
        print("password", password)

        return "<h1>You are registered Now</h1>"

    return render_template("index.html", form=reg_form)


if __name__ == '__main__':
    app.run(debug=True)
