from flask import Flask, render_template, request, make_response, session, jsonify
import sqlalchemy

import datetime
from Student import Student
from DBHandler import DBHandler

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = "mysecret key"


# State Management
# Http is stateless Protocol
# Cookies (Client Side)
# Session ( Server Side)

@app.route('/getTime')
def getTimefromServer():
    # return 'This is our first web backend response as string'
    dt = datetime.datetime.now()
    dtime = dt.strftime("%d-%M-%Y %H:%M:%S")
    return dtime


@app.route('/searchStudentsData', methods=['POST', 'GET'])
def searchStudent():
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        sname = request.args.get("sname")
        studentList = dbHdlr.searchStudents(sname)
        print(len(studentList))
        print(studentList)
        return jsonify(studentList)

    except Exception as e:
        print(str(e))
        return render_template("SearchStudent.html", error="There is some error loading students data")


@app.route('/getStudentsData')
def getStudentsData():
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        studentList = dbHdlr.fetchAllStudents()
        print(len(studentList))
        print(studentList)
        return jsonify(studentList)

    except Exception as e:
        print(str(e))
        return render_template("ShowStudents.html", error="There is some error loading students data")


@app.route('/')
def hello_world():
    # return 'This is our first web backend response as string'
    no = 10;
    no = no * 2
    dt = datetime.datetime.now()
    return render_template("Welcome.html", datetime=dt)


@app.route('/searchStudent')
def searchStudentview():
    return render_template("SearchStudent.html")


@app.route('/gdmsg')
def goodDayMessage():
    return " Good Day"


@app.route('/showstudents')
def showStudents():
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    '''
    school=request.cookies.get("School")
    print(school)
    if request.cookies.get("name") !=None:
        name = request.cookies.get("name")
    if request.cookies.get("rollno") !=None:
        rollno = request.cookies.get("rollno")
    '''
    if session.get("name") != None and session.get("rollnum") != None:
        name = session["name"]
        rollno = session["rollnum"]
    else:
        msg = "Please login"
        return render_template("ShowStudents.html", error=msg)
    try:
        name = session["name"]
        rollno = session["rollnum"]
        session.pop("cgpa")
        studentList = dbHdlr.fetchAllStudents()
        return render_template("ShowStudents.html", studentsList=studentList, name=name, rollno=rollno)

    except Exception as e:
        return render_template("ShowStudents.html", error="There is some error loading students data")


@app.route('/searchStudents')
def searchStudents():
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    try:
        studentList = dbHdlr.fetchAllStudents()
        return render_template("ShowStudents.html", studentsList=studentList, )

    except Exception as e:
        return render_template("ShowStudents.html", error="There is some error loading students data")


@app.route('/firstFormProcessor', methods=["GET", "POST"])
def firstFormProcessor():
    name = request.form["n"]
    rollno = request.form["rn"]
    sem = request.form["sem"]
    cgpa = request.form["cgpa"]
    stu = Student(name, rollno, sem, cgpa)
    dbHdlr = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    insert = dbHdlr.insertRecord(stu)
    # Session Management
    session["name"] = name
    session["rollnum"] = rollno
    session["semmester"] = sem
    session["cgpa"] = cgpa
    if insert:
        return render_template("Registration.html", name=name)
        '''
        response = make_response(render_template("Registration.html", name=name))
        response.set_cookie('name',name )
        response.set_cookie('rollno', rollno)
        response.set_cookie('semmester', sem)
        response.set_cookie('cgpa', cgpa)
        return response
        '''

    else:
        return render_template("Welcome.html", error="error inserting record")


@app.route("/logout")
def logout():
    session.clear();
    return render_template("Welcome.html", error="GoodBye")


if __name__ == '__main__':
    app.run()
