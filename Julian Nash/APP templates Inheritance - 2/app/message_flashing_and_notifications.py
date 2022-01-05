from app import app
from flask import render_template, request, redirect
from flask import flash

"""
Flashing provides us with a simple and flexible way to provide users with valuable feedback and can be styled freely.
Using filters allows us to customize flashes depending on the category passed to it, keeping users happy and notified!

syntax:
flash(message , category)

example:
flash("Account created!", "success")

"""

# https://pythonise.com/series/learning-flask/flask-message-flashing
# https://www.youtube.com/watch?v=T1PLBEEZU8o&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L&index=17

@app.route("/sign-up-two", methods=["GET", "POST"])
def sign_up_two():
     
    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")
        print(username,email,password)
        if not len(password) >= 10:
            flash("Password must be at least 10 characters", "warning")
            #  i have use base template for flash coding  
            return redirect(request.url)

        flash("Account created!", "success")
        flash("just Testing !", "danger")

        return redirect(request.url)

    return render_template("public/sign_up_two.html")
"""
We call ( with messages = get_flashed_messages()  ) to register any flashed messages
{% if messages %} then checkes to see if there are any messages in the queue
{% for message in messages %} iterates over the messages (you can call flash more then once to register several messages)
We can then do something with the contents of the message using {{ message }}

Flash categories **********************
Flask's Flash function takes up to 2 arguments, a message and a category:

flash("message", "category")

Passing  (  with_categories=true  )  to get_flashed_messages(), we're able to access the category of that flash
{% for category, message in messages %} unpacks the message and category, which we can then access within the for loop

alert-success will trigger a green alert
alert-warning will trigger an orange alert
alert-danger will trigger a red alert

"""
