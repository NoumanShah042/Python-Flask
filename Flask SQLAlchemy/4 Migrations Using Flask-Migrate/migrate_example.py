from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4556029@localhost:3307/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
manager = Manager(app)

# connect script manager and flask manager
manager.add_command('db', MigrateCommand)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))


if __name__ == '__main__':
    manager.run()


# python migrate_example.py db init
# python migrate_example.py db migrate
# python migrate_example.py db upgrade
#
