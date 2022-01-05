from flask import Flask, render_template, request
import datetime
from Student import Student
from DBHandler import DBHandler
app = Flask(__name__)
app.config.from_object("config")


@app.route('/')
def hello_world():
    # return 'This is our first web backend response as string'
    no = 10
    no = no*2
    dt = datetime.datetime.now()
    return render_template("Welcome.html", datetime=dt)


@app.route('/msg')
def goodDayMessage():
    return " Good Day"


@app.route('/showstudents')
def showStudents():
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        studentList = dbHdlr.fetchAllStudents()
        return render_template("ShowStudents.html", studentsList=studentList)

    except Exception as e:
        return render_template("ShowStudents.html", error="There is some error loading students data")


@app.route('/firstFormProcessor', methods=["GET", "POST"])
def firstFormProcessor():
    if request.method == "POST":
        name = request.form["n"]
        rollno = request.form["rn"]
        sem = request.form["sem"]
        cgpa = request.form["cgpa"]
        stu = Student(name, rollno, sem, cgpa)
        dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                           app.config["DB_PASSWORD"], app.config["DATABASE"])
    insert = dbHdlr.insertRecord(stu)
    if insert:
        return render_template("Registration.html", name=name)
    else:
        return render_template("Welcome.html", error="error inserting record")


if __name__ == '__main__':
    app.run()
