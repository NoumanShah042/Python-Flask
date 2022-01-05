import pymysql
from donor import Donor


class DBHandler:
    def __init__(self, dbipaddress, dbuser, dbpwd, dbname):
        self.dbipaddress = dbipaddress
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbname = dbname

    def addDonor(self, name, blood_group, phone, cnic, city):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into donors(`name`,`blood group`,`phone` ,`cnic`, `city`) values(%s,%s,%s,%s,%s)"
            args = (name, blood_group, phone, cnic, city)
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

    def fetch_all_donors(self):
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

    def getAvailabeDonors(self, blood_group):
        db = None
        cursor = None
        result_list = []
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            if blood_group:
                query = "select * from donors where `blood group` = %s "
                args = (blood_group,)
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
