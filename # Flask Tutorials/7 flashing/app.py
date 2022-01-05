from flask import Flask, render_template, request, flash, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

app.secret_key = "cairocoders-ednalan23"

# https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None;
    if request.method == "POST":
        if request.form['pass'] != '1234':
            error = "invalid password"
        else:
            flash("you are successfuly logged in", "success")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)