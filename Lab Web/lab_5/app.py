from flask import Flask, render_template, request
from donor import Donor
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object("config")


@app.route('/')
def menu():
    return render_template("menu.html")


@app.route('/new')
def form_display():
    return render_template("add donor.html")


@app.route('/insert', methods=["GET", "POST"])
def insert_donor():
    insert = False
    if request.method == 'POST':
        name = request.form["name"]
        bg = request.form["bg"]
        phone = request.form["phone"]
        cnic = request.form["cnic"]
        city = request.form["city"]
        donor_ = Donor(name, bg, phone, cnic, city)
        if donor_.data_validation():
            db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                           app.config["DB_PASSWORD"], app.config["DATABASE"])
            insert = db.insertRecord(donor_)
    if insert:
        return  render_template("add donor.html", msg="Donor added successfully")
    else:
        return  render_template("add donor.html", msg="Error Occurred")


@app.route('/search')
def search():
    db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                   app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        result = db.fetchAllStudents()
        return render_template("search.html", result_set=result)
    except Exception as e:
        return render_template("search.html", error="Error in searching")


@app.route('/search_data', methods=["GET", "POST"])
def get_output():
    db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                   app.config["DB_PASSWORD"], app.config["DATABASE"])

    if request.method == 'POST':
        name = request.form["name"]
        bg = request.form["bg"]
        phone = request.form["phone"]
        city = request.form["city"]
        try:
            result = db.search(name, bg, phone, city)
            return render_template("search.html", result_set=result)
        except Exception as e:
            return render_template("search.html", error="There is some error loading students data")


if __name__ == '__main__':
    app.run(debug=True)
