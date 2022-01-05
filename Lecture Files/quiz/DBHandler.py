import pymysql
from attendance import Attendance
from datetime import datetime


class DBHandler:
    def __init__(self, dbipaddress, dbuser, dbpwd, dbname):
        self.dbipaddress = dbipaddress
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbname = dbname

    def insertAttendanceRecord(self, Attendance):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            # Stu_RollNo, Stu_Name, Attendance_Course, Attendance_Date, Attendance_Status
            query = "insert into `attendance`(Stu_RollNo,Stu_Name,Attendance_Course,Attendance_Date,Attendance_Status) values(%s,%s,%s,%s,%s)"
            args = (
            Attendance.Stu_RollNo, Attendance.Stu_Name, Attendance.Attendance_Course, Attendance.Attendance_Date,
            Attendance.Attendance_Status)
            cursor.execute(query, args)
            db.commit()
            insert = True
        except Exception as e:
            print("Exception occured")
            print(e)
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return insert


db = DBHandler("localhost", "root", "", "bcs")
today = datetime.now()
att = Attendance('bcsf18m027', 'Nouman', 'Web', today, 'P')
db.insertAttendanceRecord(att)
