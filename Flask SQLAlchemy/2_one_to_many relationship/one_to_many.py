from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4556029@localhost:3307/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
	# Specify a forward reference by relationship, backref specifies a backreference, and form a two-way reference relationship
    pets = db.relationship('Pet', backref='owner')




class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
# owner_id = db.Column(db.Integer, db.ForeignKey("person.id"), default=2)


def display_pet_with_owner():
    result = db.engine.execute(
        'select person.name , pet.name from person  join pet on person.id = pet.owner_id')
    # print(result)
    # print(type(result))
    for r in result:
        # print(type(r))
        print(r)
        print(r[0], r[1])

# from one_to_many import display_pet_with_owner
# display_pet_with_owner()

def display_person():
    result = db.engine.execute("select owner_id from pet where name='dog'")
    # print(result)
    # print(type(result))
    a = 0
    for r in result:
        a = r[0]
    
    print(a)
    print(f"select name from person where id={a}")
    result = db.engine.execute(f"select name from person where id={a}")
    for r in result:
        # print(type(r))
        print(r)
        print(r[0])

# from one_to_many import display_person
# display_person()

