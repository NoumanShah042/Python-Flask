from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

# dialect+driver://username:password@host:port/database

# mysql://root:@localhost/tech_blog   ( for simple root with no password)
# mysql://root:4556029@localhost:3307/mydatabase   ( for root with different port and having password)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4556029@localhost:3307/mydatabase'
db = SQLAlchemy(app)

#  https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data
