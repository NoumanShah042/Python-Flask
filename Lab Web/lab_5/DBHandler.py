import pymysql
from donor import Donor


class DBHandler:
    def __init__(self, dbipaddress, dbuser, dbpwd, dbname):
        self.dbipaddress = dbipaddress
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbname = dbname

    def insertRecord(self, donor):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into donors(`name`,`blood group`,`phone` ,`cnic`, `city`) values(%s,%s,%s,%s,%s)"
            args = (donor.name, donor.blood_group, donor.phone, donor.cnic, donor.city)
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

    def fetchAllStudents(self):
        # create db connection
        db = None
        cursor = None
        donor_list = []
        try:

            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            #
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "Select `name`,`blood group`,`phone` ,`cnic`, `city`  from donors"
            # args=(1)
            cursor.execute(query)
            results = cursor.fetchall()
            # print("return type", type(results))
            # print(results)

            for r in results:
                donor_list.append(Donor(r["name"], r["blood group"], r["phone"], r["cnic"], r["city"]))

        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return donor_list

    def search(self, name="", blood_group="", phone="", city=""):
        db = None
        cursor = None
        result_list = []
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            # `name`,`blood group`,`phone` ,`cnic`, `city`
            if name == "" and blood_group and phone and city:
                query = "SELECT * FROM donors WHERE `blood group` = %s AND phone LIKE %s AND city = %s"
                args = (blood_group, phone + '%', city)
            elif name == "" and blood_group and phone and city == "":
                query = "SELECT * FROM donors WHERE `blood group` = %s AND phone LIKE %s"
                args = (blood_group, phone + '%')
            elif name == "" and blood_group and phone == "" and city:
                query = f"SELECT * FROM donors WHERE `blood group` = %s AND city = %s"
                args = (blood_group, city)
            elif name == "" and blood_group and phone == "" and city == "":
                query = "SELECT * FROM donors WHERE `blood group` = %s"
                args = (blood_group)
            elif name == "" and blood_group == "" and phone and city:
                query = "SELECT * FROM donors WHERE phone LIKE %s AND city = %s"
                args = (phone, city)
            elif name == "" and blood_group == "" and phone and city == "":
                query = "SELECT * FROM donors WHERE phone LIKE %s"
                args = (phone + '%')
            elif name == "" and blood_group == "" and phone == "" and city:
                query = "SELECT * FROM donors WHERE city = %s"
                args = (city)
            elif name and blood_group and phone and city:
                query = "SELECT * FROM donors WHERE `name` LIKE %s AND `blood group` = %s AND phone LIKE (%s) AND city = %s"
                args = ('%' + name + '%', blood_group, phone + '%', city)
            elif name and blood_group and phone and city == "":
                query = "SELECT * FROM donors WHERE name LIKE %s AND `blood group` = %s AND phone LIKE %s"
                args = ('%' + name + '%', blood_group, phone + '%')
            elif name and blood_group and phone == "" and city:
                query = "SELECT * FROM donors WHERE name LIKE %s AND `blood group` = %s AND city = %s"
                args = ('%' + name + '%', blood_group, city)
            elif name and blood_group and phone == "" and city == "":
                query = "SELECT * FROM donors WHERE name LIKE %s AND `blood group` = %s"
                args = ('%' + name + '%', blood_group)
            elif name and blood_group == "" and phone and city:
                query = "SELECT * FROM donors WHERE name LIKE %s AND phone LIKE %s AND city = %s"
                args = ('%' + name + '%', phone + '%', city)
            elif name == "" and blood_group and phone == "" and city:
                query = "SELECT * FROM donors WHERE `blood group` = %s AND city = %s"
                args = (blood_group, city)
            elif name and blood_group == "" and phone == "" and city:
                query = "SELECT * FROM donors WHERE name LIKE %s AND city = %s"
                args = ('%' + name + '%', city)
            elif name and blood_group == "" and phone == "" and city == "":
                query = "SELECT * FROM donors WHERE name LIKE %s"
                args = ('%' + name + '%')
            else:
                raise Exception("REQUIRED ATLEAST ONE ATTRIBUTE")
            cursor.execute(query, args)
            result = cursor.fetchall()
            for r in result:
                result_list.append(Donor(r["name"], r["blood group"], r["phone"], r["cnic"], r["city"]))
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return result_list




# db = DBHandler("localhost", "root", "", "db_flask")
# name, blood_group, phone, city
# res= db.search('', '', '0342', '')

# for r in res:
#     print(r.name, r.blood_group, r.city, r.phone, r.cnic)
# donr = Donor('Humza', 'AB+', '0342-4354654', '32432-5432432-3', 'Karachi')
# print(db.insertRecord(donr))

# res = db.fetchAllStudents()
# for r in res:
#     print(r.name ,  r.blood_group, r.city, r.phone,r.cnic )
