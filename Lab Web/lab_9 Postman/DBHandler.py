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

    def fetchStudent(self):
        # create db connection
        db = None
        cursor = None
        donor_list = []
        try:

            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            #
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "Select *  from donors"
            # args=(1)
            cursor.execute(query)
            result = cursor.fetchone()
            print("return type", type(result))
            print(result)


        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return result

    def deleteStudent(self, id):
        # create db connection
        db = None
        cursor = None
        donor_list = []
        try:

            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            #
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = r"delete from donors where id='%s'"
            args = (id,)
            cursor.execute(query, args)
            db.commit()


        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()

    def UpdateStudent(self, id, name):
        # create db connection
        db = None
        cursor = None
        donor_list = []
        try:

            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            #
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = f"update  donors set name='{name}' where id={id}"
            # args = (name, id)
            cursor.execute(query)
            db.commit()


        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()


# update  donors set name='ali' where id='%s'


db = DBHandler("localhost", "root", "", "db_flask")
# donr = Donor('Humza ALi', 'AB+', '0342-4354654', '32432-5432432-3', 'Karachi')
# db.deleteStudent(24)
db.UpdateStudent(22, 'ALi')
# name, blood_group, phone, city
# res= db.search('', '', '0342', '')

# for r in res:
#     print(r.name, r.blood_group, r.city, r.phone, r.cnic)
# donr = Donor('Humza', 'AB+', '0342-4354654', '32432-5432432-3', 'Karachi')
# print(db.insertRecord(donr))

# res = db.fetchStudents()
# # print("hell")
# for k,v in res.items():
#     # print(r.name ,  r.blood_group, r.city, r.phone,r.cnic )
#     print(k,v)
