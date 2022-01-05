import pymysql
from users import User


class User_DBHandler:
    def __init__(self, dbipaddress, dbuser, dbpwd, dbname):
        self.dbipaddress = dbipaddress
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbname = dbname

    def insertRecord(self, usr):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into users(`name`, `email`, `gender`, `password`) values(%s,%s,%s,%s)"
            args = (usr.name, usr.email, usr.gender, usr.password)
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

    def fetchAllUsers(self):
        # create db connection
        db = None
        cursor = None
        users_list = []
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "Select `name`, `email`,`gender` , `password`  from `users`"
            cursor.execute(query)
            results = cursor.fetchall()
            # print("return type", type(results))
            # print(results)

            for r in results:
                users_list.append(User(r["name"], r["email"], r["gender"],r["password"]))
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return users_list




# db = User_DBHandler("localhost", "root", "", "db_flask")
# usr = User("Ahad", "AHad@gmail.com", "male", "paasshdhd")
# db.insertRecord(usr)

