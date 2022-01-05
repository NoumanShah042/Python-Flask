from app import app
from flask import render_template, request, redirect
from flask import jsonify, make_response
from datetime import datetime

# Cookies play an important role in most modern websites and web applications, allowing us leave small strings 
# of key/value pairs on the clients browser to help both developers and users by temporarily preserving inportant
#  information such as preferences, unique identifiers, state etc..

@app.route("/cookies")
def work_with_cookies():

    res = make_response("Working with Cookies")

    res.set_cookie(
        "flavor",
        value="chocolaty chip",
        max_age=10,
        expires=None,
        path=request.path,
        domain=None,
        secure=False,
        httponly=False,
        samesite=None
    )

    res.set_cookie("vanilla", "crispy")
    res.set_cookie("magnet", "Jelly")

    print(request.cookies)
    # ImmutableMultiDict([('vanilla', 'crispy'), ('magnet', 'Jelly')])
    cookies = request.cookies  # it returns a dictionary object of all cookies
    
    flavor = cookies.get("flavor")
    vanilla = cookies.get("vanilla")
    magnet = cookies.get("magnet")
    print(flavor, vanilla, magnet)
    return res

    
