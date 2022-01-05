from flask import Flask, render_template, request, jsonify
from donor import Donor
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object("config")


#  http://127.0.0.1:5000/
@app.route('/')
def menu():
    db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                   app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        result = db.fetchStudent()
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": "error Occurred"})


#
# {
#     "blood group": "O+",
#     "city": "Lahore",
#     "cnic": "35164-8114371-3",
#     "name": "Nouman",
#     "phone": "0342-4159329"
# }

@app.route('/insert', methods=["POST"])
def insert_donor():
    insert = False
    try:
        json = request.json
        name = json["name"]
        bg = json["blood group"]
        phone = json["phone"]
        cnic = json["cnic"]
        city = json["city"]
        donor_ = Donor(name, bg, phone, cnic, city)
        if donor_.data_validation():
            db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                           app.config["DB_PASSWORD"], app.config["DATABASE"])
            insert = db.insertRecord(donor_)
            return jsonify({"message": "Record added"})
    except:
        return jsonify({"message": "Error Occured"})


#  http://127.0.0.1:5000/delete/23
@app.route('/delete/<int:id>', methods=["DELETE"])
def delete_donor(id):
    insert = False
    try:
        db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
        insert = db.deleteStudent(id)
        return jsonify({"message": "Record Deleted"})
    except:
        return jsonify({"message": "Error Occured"})


@app.route('/update/<int:id>/<string:name>', methods=["PUT"])
def update_donor(id,name):
    insert = False
    try:
        db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
        insert = db.UpdateStudent(id, name)
        return jsonify({"message": "Record Updated"})
    except:
        return jsonify({"message": "Error Occured"})


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
