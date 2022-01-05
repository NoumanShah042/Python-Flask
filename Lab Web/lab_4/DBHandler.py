# print("hello")

import pymysql


class DBHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def input_email(self):
        email1 = input("Email as xxxxx@xxxx.xxx :")
        while (email1.find('@') == -1) or (email1.find('.') == -1) or len(email1[email1.find('.') + 1:]) > 3:
            email1 = input("input Valid email:")
        return email1

    def input_roll(self):
        deg = ['cs', 'se', 'it']
        sec = ['m', 'a']
        while True:  # only take bcs bse or bit
            roll = input("Input Roll:").lower()
            if len(roll) != 10 or roll[0] != "b":
                continue
            if roll[1:3] not in deg or roll[6] not in sec:
                continue
            if roll[3] != "f":
                continue
            if not roll[4:6].isnumeric():
                continue
            if not roll[-3:].isnumeric():
                continue
            return roll

    def inputStudent(self):
        roll = self.input_roll()
        name = input("Enter Name :")
        while len(name) <= 0:
            name = input("Enter Name Again:")
        phone = input("Enter Phone :")
        while len(phone) != 11 or (not phone.isnumeric()):
            phone = input("Enter Phone Again:")

        email = self.input_email()
        cgpa = float(input("Enter CGPA :"))
        while not (0 <= cgpa <= 4.0):
            cgpa = float(input("Enter CGPA Again :"))
        return [roll, name, phone, email, cgpa]


    def getStudentsByName(self):
        db = None
        cursor = None
        list_of_students = []
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "select * from students order by name;"
            cursor.execute(query)
            db.commit()
            result_all = cursor.fetchall()

            for i in result_all:
                i['cgpa'] =float(i['cgpa'])
                list_of_students.append(i)
                # print(i , type(i))

            return list_of_students
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def isStudent(self, roll):
        db = None
        cursor = None
        roll = roll.lower()
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            query = "select roll from students;"
            cursor.execute(query)
            db.commit()
            result_all = cursor.fetchall()
            for i in result_all:
                if i[0].lower() == roll:
                    return True
            return False
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def getStudentData(self, roll):
        db = None
        cursor = None
        roll = roll.lower()
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            query = "select * from students where roll = %s;"
            args = (roll,)
            cursor.execute(query, args)
            db.commit()
            res = cursor.fetchone()
            data = {}

            if res is None:
                return data
            temp_roll = res[1].lower()
            data = {
                "roll": temp_roll,
                "name": res[2],
                "phone": res[3],
                "email": res[4],
                "degree": temp_roll[0] + 's',
                "course": temp_roll[1:3],
                "year": '20' + temp_roll[4:6],
                "session": "",
                "section": "",
                "campus": "",
                "roll_no": temp_roll[-2:],
                "cgpa": float(res[5]),
            }

            if temp_roll[-3] == "0":
                data["campus"] = "Old"
            elif temp_roll[-3] == "5":
                data["campus"] = "New"

            if temp_roll[-4] == "m":
                data["section"] = "Morning"
            elif temp_roll[-4] == "a":
                data["section"] = "Afternoon"

            year_start = int('20' + temp_roll[4:6])
            year_end = ""
            if data["degree"] == "bs":
                year_end = year_start + 4
            elif data["degree"] == "ms":
                year_end = year_start + 2
            data["session"] = (str(year_start) + '-' + str(year_end))

            return (data)
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def addStudent(self, roll, name, phone, email, cgpa):
        db = None
        cursor = None
        list_of_students = []
        if self.isStudent(roll):
            return False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into students(roll,name,phone,email,cgpa) values(%s,%s,%s,%s,%s);"
            args = (roll, name, phone, email, cgpa)
            cursor.execute(query, args)
            db.commit()
            return True
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def deleteStudent(self, roll):
        db = None
        cursor = None
        if not self.isStudent(roll):
            return False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "delete from students where roll = %s;"
            args = (roll,)
            cursor.execute(query, args)
            db.commit()
            return True
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def getHighestCGPA(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            query = "select * from students where cgpa=(select max(cgpa) from students);"
            cursor.execute(query)
            db.commit()
            result = cursor.fetchone()
            if result == None:
                return False
            dic = {}
            dic["roll"] = result[1]
            dic["email"] = result[4]
            dic["cgpa"] = float(result[5])

            return dic
        except Exception as e:
            print("Exception occurred")
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def updateStudent(self, roll, new_name, new_phone, new_email, new_cgpa):
        if not self.isStudent(roll):
            return False
        std_data = self.getStudentData(roll)

        if len(new_name) != 0:
            std_data["name"] = new_name
        if len(new_phone) != 0:
            std_data["phone"] = new_phone
        if len(new_email) != 0:
            std_data["email"] = new_email
        if new_cgpa != -1:
            std_data["cgpa"] = new_cgpa
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            query = "UPDATE students SET name = %s, phone = %s, email = %s, cgpa = %s WHERE  roll = %s;"
            args = (std_data["name"], std_data["phone"], std_data["email"], std_data["cgpa"], roll)
            cursor.execute(query, args)
            db.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            if db is not None:
                db.close()
            if cursor is not None:
                cursor.close()


db = DBHandler(host='localhost',
               user='root',
               password='',
               database='std_db')

while True:
    print("\n\n========================================================")
    print("1. add")
    print("2. update")
    print("3. delete")
    print("4. Get Student by Name")
    print("5. Get Student data")
    print("6. isStudent")
    print("7. Get Highest CGPA")
    print("8. Exit")
    print("========================================================")
    choice = 0
    try:
        choice = int(input(":"))
    except ValueError:
        print("input a Digit")
    # print(choice)
    if choice == 1:
        print("input Student Info")
        list = db.inputStudent()
        # [roll, name, phone, email, cgpa]
        db.addStudent(list[0], list[1], list[2], list[3], list[4])

    elif choice == 2:
        print("input Student Info")
        list = db.inputStudent()
        # [roll, name, phone, email, cgpa]
        db.updateStudent(list[0], list[1], list[2], list[3], list[4])

    elif choice == 3:
        roll = db.input_roll()
        print("outPut :", db.deleteStudent(roll))

    elif choice == 4:
        dic = db.getStudentsByName()
        for i in dic:
            print(i)

    elif choice == 5:
        roll = db.input_roll()
        dic = db.getStudentData(roll)
        for key,value in dic.items():
            print(key,":",value )

    elif choice == 6:
        roll = db.input_roll()
        print(db.isStudent(roll))

    elif choice == 7:
        print("Highest CGPA: ")
        print(db.getHighestCGPA())
    elif choice == 8:
        break
    else:
        print("input Valid Choice")

# dic =db.getStudentsByName()
# print(dic)

# print(db.isStudent("bcsf18m023"))

# print(db.inputStudent())

# print(db.getStudentData("bcsf18m027"))
# print(db.getStudentData("bcsf18m017"))
# print(db.getStudentData("bcsf18a027"))

# ret = db.addStudent("mcsf18m001", "Fatima", "03231043234", "mcsf18m001@pucit.edu.pk", "3.7")
# print(ret)

# print(db.deleteStudent("bcsf18m019"))

# print(max(1.8 ,1.9,))

# print(db.getHighestCGPA())

# def updateStudent(self, roll, new_name, new_phone, new_email, new_cgpa):

# print(db.updateStudent('bcsf18m003', '', '03333333333', 'bcsf18m003@pucit.edu.pk', -1))
