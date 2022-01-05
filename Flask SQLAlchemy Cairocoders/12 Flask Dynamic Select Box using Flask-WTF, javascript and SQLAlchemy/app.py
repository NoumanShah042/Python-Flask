from flask import Flask, render_template, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from wtforms import SelectField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

db = SQLAlchemy(app)


class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))


class State(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    country_id = db.Column(db.Integer)


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    stateid = db.Column(db.Integer)


class Form(FlaskForm):
    country = SelectField('country', choices=[])
    state = SelectField('state', choices=[])
    city = SelectField('city', choices=[])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    form.country.choices = [(country.id, country.name) for country in Country.query.all()]

    if request.method == 'POST':
        city = City.query.filter_by(id=form.city.data).first()
        country = Country.query.filter_by(id=form.country.data).first()
        state = State.query.filter_by(id=form.state.data).first()
        return '<h1>Country : {}, State: {}, City: {}</h1>'.format(country.name, state.name, city.name)
    return render_template('index.html', form=form)


# >>> [(country.id, country.name) for country in Country.query.all()]
# >>> [(171, 'Philippines'), (227, 'United States of America')]    ------------ output

#               state/227
@app.route('/state/<get_state>')
def statebycountry(get_state):
    states = State.query.filter_by(country_id=get_state).all()
    stateArray = []
    for state in states:
        stateObj = {}
        stateObj['id'] = state.id
        stateObj['name'] = state.name
        stateArray.append(stateObj)
    return jsonify({'statecountry': stateArray})


@app.route('/city/<get_city>')
def city(get_city):
    state_data = City.query.filter_by(stateid=get_city).all()
    cityArray = []
    for city in state_data:
        cityObj = {}
        cityObj['id'] = city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)
    return jsonify({'citylist': cityArray})


if __name__ == '__main__':
    app.run(debug=True)
