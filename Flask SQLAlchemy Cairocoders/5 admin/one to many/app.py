from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# pip install flask_admin

# Flask admin documentation : https://flask-admin.readthedocs.io/en/latest/
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

db = SQLAlchemy(app)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'darkly'

admin = Admin(app, name='microblog', template_mode='bootstrap3')


# Add administrative views here

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))


admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Pet, db.session))

if __name__ == '__main__':
    app.run(debug=True)
