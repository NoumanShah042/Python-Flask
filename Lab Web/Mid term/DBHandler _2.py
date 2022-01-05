import pymysql

# Create Table Appointment ( appointmentID serial Primary Key,
# workerID int ,
# AppointmentStart DATETIME,
# AppointmentEnd DATETIME,
# uname varchar(255)
# );

class DBHandler:
    def __init__(self, dbipaddress, dbuser, dbpwd, dbname):
        self.dbipaddress = dbipaddress
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbname = dbname

    def addAppoinment(self, id, strat , end , uname ):
        db = None
        cursor = None
        insert = False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into users(`workerID`,`AppointmentStart`,`AppointmentEnd`,`uname` ) values(%s,%s,%s,%s)"
            args = (id, strat, end, uname)
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


