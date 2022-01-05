from flask import Flask, render_template, request, redirect
from product import Product, insert_product

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        prod_title = request.form['title']
        prod_desc = request.form['desc']
        prod_units = request.form['units']
        prod_price = request.form['price']
        # print(prod_title, type(prod_title))
        # print(prod_desc, type(prod_desc))
        # print(prod_units, type(prod_units))
        # print(prod_price, type(prod_price))

        prod = Product(1, prod_title, prod_desc, int(prod_units), int(prod_price))
        insert_product(prod)

        return render_template("index.html")
    else:
        return render_template("index.html")


# @app.route('/insert', methods=['GET', 'POST'])
# def insert():
#     if request.method == 'POST':
#         prod_title = request.form['title']
#         prod_desc = request.form['desc']
#         prod_units = request.form['units']
#         prod_price = request.form['price']
#         # print(prod_title, type(prod_title))
#         # print(prod_desc, type(prod_desc))
#         # print(prod_units, type(prod_units))
#         # print(prod_price, type(prod_price))
#         return 'hello'
#     #     prod = Product(1, "OPPO S7", 'RAM 29GB+Storage 1000GB', 40, 90000)
#     #     insert_product(prod)
#     #     return redirect('/insert')


if __name__ == "__main__":
    app.run(debug=True)
