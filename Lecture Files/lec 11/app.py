from flask import Flask, render_template, request
import datetime
from Student import Student
from DBHandler import DBHandler

app = Flask(__name__)


# Jinja modules
@app.route('/')
def hello_world():
    # return 'This is our first project Hello World!'
    dt = datetime.datetime.now()
    return render_template("Welcome.html", datetime=dt)


@app.route('/first', methods=["GET", "POST"])
def firstFormSubmission():
    nm = request.form["n"]
    rollno = request.form["rollno"]
    return render_template("FirstPage.html", name=nm, rn=rollno)


@app.route("/registerstudent")
def getRegisterationFOrm():
    return render_template("Registration.html")


# Student Register Module
@app.route('/register', methods=["GET", "POST"])
def registerStudent():
    name = request.form["n"]
    rollno = request.form["rollno"]
    sem = request.form["sem"]
    cgpa = request.form["cgpa"]
    stu = Student(name, rollno, sem, cgpa)
    dbHdlr = DBHandler("hdgudu")
    insert = dbHdlr.insertRecord(stu)
    if insert:
        return render_template("FirstPage.html", name=name, rn=rollno)
    else:
        render_template("Registration.html", error="Record not inserted")


@app.route('/message')
def gooddayMessage():
    return 'Good Day'


if __name__ == '__main__':
    app.run()
