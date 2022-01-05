from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# https://flask-wtf.readthedocs.io/en/stable/quickstart.html?highlight=datarequired
# DataRequired - means field will not be empty

# each field has a list of errors , to see if the field is valid or not

class ContactForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    language = SelectField('Programming Languages', choices=[('java', 'Java'), ('py', 'Python')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


"""
from flask_wtf import Form  
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  
   
class ContactForm(Form):  
   name = TextField("Candidate Name ",[validators.Required("Please enter your name.")])  
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])  
   Address = TextAreaField("Address")  
      
   email = TextField("Email",[validators.Required("Please enter your email address."),  
   validators.Email("Please enter your email address.")])  
      
   Age = IntegerField("Age")  
   language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')])  
   
   submit = SubmitField("Submit")  
"""
