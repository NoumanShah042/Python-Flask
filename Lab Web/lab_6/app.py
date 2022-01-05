from flask import Flask, render_template, request, session, redirect, url_for
from donor import Donor
from users import User
from DBHandler import DBHandler
from User_DBHandler import User_DBHandler

app = Flask(__name__)
app.config.from_object("config")
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

current_logged_in_user = " "


@app.route('/')
def menu():
    return render_template("sign_in.html", msg="")


@app.route('/sign_up')
def sign_up():
    list_data = ["", "", "", ""]
    return render_template("sign_up.html", list_data=list_data)


@app.route('/insert_user', methods=["GET", "POST"])
def insert_user():
    insert = False
    global current_logged_in_user
    list_data = ["", "", "", ""]
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        gender = request.form["gender"]
        password = request.form["password"]
        user = User(name, email, gender, password)
        list_data = [name, email, gender, password]
        # print(list_data)

        if len(name) <= 0 or len(name) > 20:
            return render_template("sign_up.html", list_data=list_data, msg="Invalid Name")
        if email.find('@') == -1 or (email.find('.') == -1) or (email[::-1].find('.') > 3):
            return render_template("sign_up.html", list_data=list_data, msg="Invalid Email")
        gender = gender.lower()
        if gender != "male" and gender != "female":
            return render_template("sign_up.html", list_data=list_data, msg="Invalid Gender")
        if len(password) < 8:
            return render_template("sign_up.html", list_data=list_data,
                                   msg="Password must be greater than 8 characters")

        db = User_DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                            app.config["DB_PASSWORD"], app.config["DATABASE"])
        insert = db.insertRecord(user)

    if insert:
        session["user_email"] = email
        current_logged_in_user = email
        return redirect("/show_dashboard")
    else:
        return render_template("sign_up.html", list_data=list_data, msg="Error Occurred")


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    global current_logged_in_user
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        valid_users_emails = []
        db = User_DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                            app.config["DB_PASSWORD"], app.config["DATABASE"])
        try:
            result = db.fetchAllUsers()
            for user in result:
                valid_users_emails.append(user.email)

            if email not in valid_users_emails:
                return render_template("sign_in.html", msg="User Not Found")

            user_password = ""
            for user in result:
                if email == user.email:
                    user_password = user.password
            if user_password != password:
                return render_template("sign_in.html", msg="Wrong Password")
            else:
                session["user_email"] = email
                current_logged_in_user = email
                return render_template("menu.html", email=email)

        except Exception as e:
            return render_template("sign_in.html", msg="Exception Occur")

    return render_template("sign_in.html", msg="")


@app.route('/show_dashboard')
def show_dashboard():
    global current_logged_in_user
    if session.get("user_email", None) == current_logged_in_user:
        return render_template("menu.html", email=current_logged_in_user)
    return "<h1 style='color:blue;text-align:center;'>Please Log in first</h1>"


@app.route("/sign-out")
def sign_out():
    global current_logged_in_user
    session.pop("user_email", None)
    current_logged_in_user = " "
    return render_template("sign_in.html", msg="")


@app.route('/new')
def form_display():
    global current_logged_in_user
    if session.get("user_email", None) == current_logged_in_user:
        return render_template("add donor.html", user=session.get("user_email", None))

    return "<h1 style='color:blue;text-align:center;'>Please Log in first</h1>"


@app.route('/insert', methods=["GET", "POST"])
def insert_donor():
    global current_logged_in_user
    if session.get("user_email", None) == current_logged_in_user:
        insert = False
        if request.method == 'POST':
            name = request.form["name"]
            bg = request.form["bg"]
            phone = request.form["phone"]
            cnic = request.form["cnic"]
            city = request.form["city"]

            if len(name) <= 0 or len(name) > 20:
                return render_template("add donor.html", msg="<h1 style='color:blue;'>Invalid Name</h1>",user=session.get("user_email", None))

            if len(phone) != 12 or (phone[:2] != '03') or (not phone[5:].isnumeric()) or (
                    not phone[:4].isnumeric()) or (phone[4] != '-'):
                return render_template("add donor.html", msg="<h1 style='color:blue;'>Invalid Phone</h1>", user=session.get("user_email", None))

            if bg not in ['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']:
                return render_template("add donor.html", msg="<h1 style='color:blue;'>Invalid Blood Group</h1>",
                                       user=session.get("user_email", None))
            if len(cnic) != 15 or (not cnic[:5].isnumeric()) or (not cnic[6:13].isnumeric()) or (
                    not cnic[-1].isnumeric()) or \
                    (cnic[5] != '-' or cnic[-2] != '-'):
                return render_template("add donor.html", msg="<h1 style='color:blue;'>Invalid CNIC</h1>", user=session.get("user_email", None))
            if len(city) <= 0 or len(city) > 50:
                return render_template("add donor.html", msg="<h1 style='color:blue;'>Invalid City</h1>", user=session.get("user_email", None))

            db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                           app.config["DB_PASSWORD"], app.config["DATABASE"])
            insert = db.addDonor(name, bg, phone, cnic, city)

        if insert:
            return render_template("add donor.html", msg="<h1 style='color:blue;'>Donor added successfully</h1>",
                                   user=session.get("user_email", None))
        else:
            return render_template("add donor.html", msg="<h1 style='color:blue;'>Error Occurred</h1>",
                                   user=session.get("user_email", None))
    return "<h1 style='color:blue;text-align:center;'>Please Log in first</h1>"


@app.route('/search')
def search():
    global current_logged_in_user
    if session.get("user_email", None) == current_logged_in_user:
        db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
        try:
            result = db.fetch_all_donors()
            return render_template("search.html", result_set=result, user=session.get("user_email", None),msg="")
        except Exception as e:
            return render_template("search.html", error="Error in searching", user=session.get("user_email", None),msg="")

    return "<h1 style='color:blue;text-align:center;'>Please Log in first</h1>"


@app.route('/search_data', methods=["GET", "POST"])
def get_output():
    # global current_logged_in_user
    if session.get("user_email", None) == current_logged_in_user:
        result = []
        db = DBHandler(app.config["DB_IP"], app.config["DB_USER"],
                       app.config["DB_PASSWORD"], app.config["DATABASE"])
        if request.method == 'POST':
            bg = request.form["bg"]
            if bg not in ['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']:
                return render_template("search.html", result_set=result, user=session.get("user_email", None),
                                       msg="<h1 style='color:blue;'>Invalid Blood Group </h1>")

            try:
                result = db.getAvailabeDonors(bg)
                return render_template("search.html", result_set=result, user=session.get("user_email", None), msg="")
            except Exception as e:
                return render_template("search.html", error="There is some error loading students data",
                                       user=session.get("user_email", None), msg="")

    return "<h1 style='color:blue;text-align:center;'>Please Log in first</h1>"


@app.route('/request_donors')
def request_donors():
    return "<h1 style='color:blue;text-align:center;'>Request Sent</h1>"

if __name__ == '__main__':
    app.run(debug=True)
