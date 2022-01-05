import pymysql



class DBHandler:

    def __init__(self,DATABASEIP , DB_USER , DB_PASSWORD , DATABASE):
        self.DATABASEIP = DATABASEIP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE
    def  __del__(self):
        print("Destructor")

    def signin(self,email,password):
        db = None
        cursor = None
        signin = False
        try:
            db = pymysql.connect(self.DATABASEIP, self.DB_USER, self.DB_PASSWORD, self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select  password from users where email = %s'
            args = (email)
            cur.execute(sql, args)
            for row in cur.fetchall():
                pwd=row[0]
                if password==pwd:
                    signin=True


        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.close()

            return signin

    def signup(self,email,password,fname,lname):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(self.DATABASEIP, self.DB_USER, self.DB_PASSWORD, self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'INSERT INTO users (email,password,fname,lname) VALUES (%s,%s,%s,%s)'
            args = (email, password, fname, lname)
            cur.execute(sql, args)
            insert= True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if(db!=None):
                db.commit()
                db.close()
            return insert

    def showCourses(self,email):
        db = None
        cursor = None
        coursesList = []
        try:
            db = pymysql.connect(self.DATABASEIP, self.DB_USER, self.DB_PASSWORD, self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select coursecode,batch from usercourses where user_email ='+'%s'
            args = (email)
            cur.execute(sql, args)

            for row in cur.fetchall():
                course = {}
                course["CourseCode"]=row[0]
                course["Batch"]=row[1]
                coursesList.append(course)
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if(db!=None):
                db.close()
            return coursesList


def Test():
    db = DBHandler("localhost", "root", "m@vra123","attomus")
    db.signup("tom@yahoo.com", "123", "Tom", "Jerry")

if __name__ == '__main__':
    Test()





