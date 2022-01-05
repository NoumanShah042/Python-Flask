# import pymysql.cursors
import pymysql


def fetchAllrecords():
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        # db = pymysql.connect("localhost","root","m@vra123","test")
        db = pymysql.connect(host='localhost', user='root', password='m@vra123', database='test')
        # Create cursor object
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "Select id,rollno,semmester  from students"
        # args=(1)
        cursor.execute(query)
        # Get results through Cursor
        result = cursor.fetchone()
        print("id", result["id"])
        print("rollno", result["rollno"])
        print("semmester", result["semmester"])
        # print("semester", result[3])
        # print("cgpa",result[4])
        # cursor.rownumber=0
        results = cursor.fetchall()
        print("return type", type(results))
        print(results)
        for r in results:
            print("id", r["id"], "rollno", r["rollno"], "semmester", r["semmester"])

    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()


def fetchStudentBySemmester(semmester, cgpa):
    # create db connection
    db = None
    cursor = None
    students = []
    try:
        # create db connection
        # db = pymysql.connect("localhost","root","m@vra123","test")
        db = pymysql.connect(host='localhost', user='root', password='m@vra123', database='test')
        # Create cursor object
        cursor = db.cursor()
        query = "Select id,rollno,semmester,cgpa  from students where semmester=%s and cgpa >= %s"
        args = (semmester, cgpa)
        cursor.execute(query, args)
        results = cursor.fetchall()
        print("return type", type(results))
        print(results)
        for r in results:
            student = {}
            student.update(id=r[0])
            student.update(rollno=r[1])
            student.update(semmester=r[2])
            student.update(cgpa=r[3])
            students.append(student)
            print("id", r[0], "rollno", r[1], "semmester", r[2], "CGPA", r[3])

    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()
        return students


'''
students=fetchStudentBySemmester(5,3)
for s in students:
    print(s)
'''


def insertRecord(studentDic):
    db = None
    cursor = None
    try:
        db = pymysql.connect(host="localhost", user="root", password="m@vra123", database="test")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "insert into students(rollno,name,semmester,cgpa) values(%s,%s,%s,%s)"
        print("semmester datatype", type(studentDic["semmester"]))
        print("cgpa datatype", type(studentDic["cgpa"]))
        if (len(studentDic) == 2):
            args = (studentDic["rollno"], studentDic["name"])

        else:
            args = (studentDic["rollno"], studentDic["name"], studentDic["semmester"], studentDic["cgpa"])

        cursor.execute(query, args)
        db.commit()
    except Exception as e:
        print("Exception occured")
        print(e)
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()


student = {"rollno": "BSCSF18M001", "name": "Ali", "semmester": 5, "cgpa": 3}
insertRecord(student)
fetchAllrecords()
