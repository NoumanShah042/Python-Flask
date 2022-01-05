# The Flask session object - Python on the web - Learning Flask Series Pt. 16  ********************************

# session object is available globally
# so all of our routes can access session object  ( unless import session  )
# even we can access session in our jinja templates in html files


# session.get("key" , None )  ----  we will get None if key not exist in session dictionary
# session.get("key" , "anything" )   ---- we will get a string if key not exist in session dictionary

""" 

https://pythonbasics.org/flask-sessions/

https://pythonise.com/series/learning-flask/flask-session-object

Sessions in Flask are a way to store information about a specific user from one request to the next. They work by storing a 
cryptographically signed cookie on the users browser and decoding it on every request.

The sesison object can be treated just like a dictionary that persists across requests, making it an ideal place to store non sensitive user data.


Important :

The session object is NOT a secure way to store data. It's a base64 encoded string and can easily be decoded, thus not making it a secure way to save or access sensitive information.

We'll demonstrate decoding a session cookie shortly.

In this example, we're going to create a very unsecure system to allow users to log in and view their profile.

The purpose is to demonstrate the session object, not a secure user management system! This guide doesn't include any password hashing, user feedback or even a real database, it's purely for the demonstration of working with sessions.

"""

# *********************************

from app import app
from flask import render_template, request, session, redirect, url_for
# render_template - Allows us to render a template to the browser
# request - To handle the incoming form data and URL
# session - The session object
# redirect - Allows us to redirect users to various parts of our app
# url_for - Constructs URL's from arguments

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"
# The session object requires your app to have a value set for the SECRET_KEY variable
# The secret key is used to encode the session cookie, so it's advised to use something relitively complex.


users = {
    "julian": {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "example",
        "bio": "Some guy from the internet"
    },
    "clarissa": {
        "username": "clarissa",
        "email": "clarissa@icloud.com",
        "password": "sweetpotato22",
        "bio": "Sweet potato is life"
    }
}

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        password = req.get("password")

        if not username in users:    
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]

        if not password == user["password"]:
            print("Incorrect password")
            return redirect(request.url)
        else:
            session["USERNAME"] = user["username"]      # we are adding key and value pair to session object ( dictionary )
            # session["PASSWORD"] = user["password"]

            print("User Added to session")
            print(session)  # <SecureCookieSession {'USERNAME': 'julian'}>

            # return redirect(request.url)
            return redirect(url_for("user_profile"))   # url_for takes the function name here

    return render_template("public/sign_in.html")
    # print(request.path)      # /sign-in
    # print(request.url)      # http://127.0.0.1:5000/sign-in
    

@app.route("/user_profile")
def user_profile():
    
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("public/profile2.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("sign_in"))   # sign_in is the name of our function


@app.route("/sign-out")
def sign_out():

    session.pop("USERNAME", None)
    # We pass None to session.pop to make sure if a user who isn't signed in visits the sign out route, 
    #       they will also be redirected to the sign in route without the application throwing an error.
    # Without None, the application throws a KeyError.

    return redirect(url_for("sign_in"))
