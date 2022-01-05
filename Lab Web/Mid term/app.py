from flask import Flask, render_template , request
from DBHandler import DBHandler

app = Flask(__name__)

@app.route('/')
def show_page():
    return render_template("registration.html")


@app.route('/registeru', methods=["GET", "POST"])
def insert_user():
    insert = False

    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]

        password = request.form["password"]

        if len(name) <= 0 or len(name) > 20:
            return render_template("registration.html", msg="Invalid Name")
        if email.find('@') == -1 or (email.find('.') == -1) or (email[::-1].find('.') > 3):
            return render_template("registration.html", msg="Invalid Email")
        if len(password) < 8:
            return render_template("registration.html",
                                   msg="Password must be greater than 8 characters")

        db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
        insert = db.addUser(1, name, email, password)

    if insert:
        return render_template("welcome.html")
    else:
        return render_template("registration.html", msg="Error Occurred")


if __name__ == '__main__':
    app.run(debug=True)
