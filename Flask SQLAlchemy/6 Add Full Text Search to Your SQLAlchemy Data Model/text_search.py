from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_whooshalchemy import WhooshAlchemy  
 
from flask_whooshalchemy import flask_whooshalchemy

app = Flask(__name__)
db = SQLAlchemy(app)


# set the location for the whoosh index
app.config['WHOOSH_BASE'] = 'whoosh'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4556029@localhost:3307/rough'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True


class Course(db.Model):

    __searchable__ = ['title', 'content']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    descriptoin = db.Column(db.String(50))


# wa.whoosh_index(app, Course)
