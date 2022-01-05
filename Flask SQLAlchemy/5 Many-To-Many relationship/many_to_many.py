from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# https://www.youtube.com/watch?v=OvhoYbjtiKc

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4556029@localhost:3307/relationship'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# ralationship table
subs = db.Table('subs',
                db.Column('user_id', db.Integer,
                          db.ForeignKey('user.user_id')),
                db.Column('channel_id', db.Integer,
                          db.ForeignKey('channel.channel_id'))
                )


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # subscriptions relate both tables
    subscriptions = db.relationship(
        'Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20))


"""

execute custom queries SQL

this technique can run for avery database sqlite , mysql etc


******************************

>>> r  = db.engine.execute('select user_id , name from user')
>>> for i in r:
...     i
...
(1, 'Nouman')
(2, 'Farhan')
(3, 'ALi')
(4, 'Humza')
>>>  

******************************  

>>>  r  = db.engine.execute('insert into user( user_id , name) values(6 , "haider")')
>>>  db.session.commit()

       
******************************
"""
