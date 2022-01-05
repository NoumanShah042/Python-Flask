from datetime import datetime


# Create a class named Attendance having following attributes Stu_RollNo, Stu_Name ,
# Attendance_Course , Attendance_Date , Attendance_Status , Make sure that Attendance_
# Date should not be future or past date in that case raise FutureORPreviousDateException.
# write member function named print which will values of all attributes.

class Attendance:
    def __init__(self, Stu_RollNo, Stu_Name, Attendance_Course, Attendance_Date, Attendance_Status):
        self.Stu_RollNo = Stu_RollNo
        self.Stu_Name = Stu_Name
        self.Attendance_Course = Attendance_Course
        self.Attendance_Date = Attendance_Date
        self.Attendance_Status = Attendance_Status

    def print(self):
        print('Student Roll no: ', self.Stu_RollNo)
        print('Student Name: ', self.Stu_Name)
        print('Attendance_Course: ', self.Attendance_Course)
        print('Attendance_Date: ', self.Attendance_Date)
        print('Attendance_Status: ', self.Attendance_Status)





# today = datetime.now()
# a = Attendance('bcsf18m027', 'Nouman', 'web', today, 'P')
# a.print()
