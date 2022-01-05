from attendance import Attendance
from datetime import datetime


def takeRecord():
    Stu_RollNo = input('\nStudent Roll no: ')
    Stu_Name = input('Student Name: ')
    Attendance_Course = input('Attendance_Course:')
    try:
        my_string = str(input('Attendance_Date(yyyy-mm-dd hh:mm): '))
        Attendance_Date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
    except Exception as e:
        print("Exception occured")
        print(e)

    Attendance_Status = input('Attendance_Status: ')
    att = Attendance(Stu_RollNo, Stu_Name, Attendance_Course, Attendance_Date, Attendance_Status)
    return att


def make_collection():
    collection_list = []
    for i in range(10):
        collection_list.append(takeRecord())
    return collection_list


# print(make_collection())
print(takeRecord().print())
