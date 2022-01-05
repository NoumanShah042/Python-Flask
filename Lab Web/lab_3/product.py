import pymysql


class Product:

    def __init__(self, pid, title, des, units, price):
        self.product_id = pid
        self.product_title = title
        self.product_des = des
        if units >= 0:
            self.product_units = units
        else:
            self.product_units = 0

        if price >= 0:
            self.product_price = price
        else:
            self.product_price = 0


def insert_product(prod):
    db = None
    cursor = None
    try:

        db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='mobile_shop')
        cursor = db.cursor()
        query = "insert into  products(product_title,product_des,product_units,product_price) values(%s,%s,%s,%s)"
        args = (prod.product_title, prod.product_des, prod.product_units, prod.product_price)

        cursor.execute(query, args)
        db.commit()
    except Exception as e:
        print("Exception occured")
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


# prod = Product(1, "OPPO S7", 'RAM 29GB+Storage 1000GB', 40, 90000)
# insert_product(prod)

# *********************************************************************
# *********************************************************************

def product_units_less_than(units):
    db = None
    cursor = None
    results = None
    list_of_products = []
    try:
        db = pymysql.connect(host='localhost', user='root', password='', database='mobile_shop')
        cursor = db.cursor()
        query = "select * from products where product_units < %s"
        args = (units,)
        cursor.execute(query, args)
        db.commit()
        results = cursor.fetchall()
    except Exception as e:
        print("Exception occurred")
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    for p in results:
        temp_prod = Product(p[0], p[1], p[2], p[3], p[4])
        list_of_products.append(temp_prod)
    return list_of_products


# lst = product_units_less_than(65)
# for pr in lst:
#     print(pr.product_id, pr.product_title, pr.product_des, pr.product_units, pr.product_price)

# *********************************************************************
# *********************************************************************

def delete_product(pid):
    db = None
    cursor = None
    results = None
    try:
        db = pymysql.connect(host='localhost', user='root', password='', database='mobile_shop')
        cursor = db.cursor()
        query = "delete from products where product_id = %s"
        args = (pid,)
        cursor.execute(query, args)
        db.commit()
    except Exception as e:
        print("Exception occurred")
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

# delete_product(3)
