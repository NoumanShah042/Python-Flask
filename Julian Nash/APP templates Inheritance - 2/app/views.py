from app import app
from flask import render_template, request, redirect , abort
from flask import jsonify, make_response
from datetime import datetime


# ImmutableMultiDict -> special class of dictionary ,with keys and values, nicely serialized which we can treat just like a Python dictionary
# request.get_json() ->   convert incomming json object to  python dictionary 
# jsonify -> convert python  dictionary to json object

@app.route("/")
def index():
     
    # print(app.config["DB_NAME"])
    # print(f'ENV is set to: {app.config["ENV"]}')
    # print(app.config["ENV"])

    # print(app.config)
    # for k,v in app.config.items():
    #     print(k,":",v) 
    return render_template("public/index.html")

# @app.route("/")
# def index():
#     return "Hello world"


# custom filter take date and show in ( 03 Apr 2021 ) format
@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")  # 03 Apr 2021


@app.route("/jinja")  # jinja templating
def jinja():

    # Strings
    my_name = "Nouman"

    # Integers
    my_age = 30

    # html string
    my_html = "<h1>This is some HTML</h1>"

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Ali": 43,
        "Humza": 28,
        "Syed": 26,
        "Farhan": 23,
        "Fatima": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    bool_var = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    return render_template("public/jinja.html", var1=my_name, my_age=my_age, langs=langs,
                           friends=friends, colors=colors, bool_var=bool_var, GitRemote=GitRemote,
                           my_remote=my_remote, repeat=repeat, date=date, my_html=my_html, suspicious=suspicious
                           )


@app.route('/submit')
def sub():
    print("submitted")
    return "submitted"


@app.route("/about")
def about():
    return "<h1 style='color: red;'>About !!!</h1>"


# Forms with Flask - Python on the web - Learning Flask Series Pt 7   ********************************

# @app.route("/sign-up", methods=["GET", "POST"])
# def sign_up():

#     if request.method == "POST":

#         req = request.form    # return a <class 'werkzeug.datastructures.ImmutableMultiDict'>
#         # print(type(req))

#         username = req.get("username")
#         email = req["email"]
#         password = request.form["password"]

#         # You could also use
#         password = request.form.get("password")

#         print(username)
#         print(email)
#         print(password)

#         # print(request.url)  #  will return current url http://127.0.0.1:5000/sign-up
#         return redirect(request.url)

#     return render_template("public/sign_up.html")


@app.route("/sign-up", methods=["GET", "POST"])  # from handling
def sign_up():
    # this method can accept get request and can accept post request
    list_data = []
    if request.method == "POST":
    
        print("sign_up\n")
        req = request.form    # return a <class 'werkzeug.datastructures.ImmutableMultiDict'>
        # print(type(req))

        username = req.get("username")
        email = req["email"]
        password = request.form["password"]

        # You could also use
        password = request.form.get("password")

        list_data = [username, email, password]

        print(username)
        print(email)
        print(password)

        # return render_template(request.url, list_data=list_data)
        return render_template("public/sign_up.html", list_data=list_data)

    return render_template("public/sign_up.html", list_data=list_data)



# Dynamic URL's with Flask - Python on the web - Learning Flask Series Pt. 8    ********************************
# for dynamic variables , see sending_files.py tutorial or text file( imp Flask basic codes)

# @app.route("/profile")
# def profile():
#     return render_template("public/profile.html")


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    },
    "nouman": {
        "name": "Syed Nouman",
        "bio": "Student AT PUCIT/FCIT",
        "twitter_handle": "@noumanshah"
    }
}

@app.route('/profile')
def profile1():
   return "<h1>use /profile/username</h1>"



@app.route("/profile/<username>")    # dynamic url's
def profile(username):
    # print(username)
    # if username in users:
    #     print(users[username])
    # else:
    #     print("not Found")
    user = None

    if username in users:
        user = users[username]
        # print("user", user)       # user {'name': 'Syed Nouman', 'bio': 'Student AT PUCIT/FCIT', 'twitter_handle': '@noumanshah'}
        # print("type",type( user)) # type < class 'dict' >

    return render_template("public/profile.html", username=username, user=user)


# http://127.0.0.1:5000/multiple/nomi/28/pucit
@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):
    # we have full access to the variables captured in the URL and passed into our function!
    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")
    return f"foo is {foo} , bar is {bar}, baz is {baz}"



# JSON with Flask - Python on the web - Learning Flask Series Pt. 9       ********************************


# @app.route("/json", methods=["POST"])
# def json_example():
#     # Validate the request body contains JSON (validate that any json is coming to our route)
#     if request.is_json:
#         # Parse the JSON into a Python dictionary
#         req = request.get_json()
#         # Print the dictionary
#         print(req)
#         # Return a string along with an HTTP status code
#         return "JSON received!", 200
#     else:
#         # The request body wasn't JSON so return a 400 HTTP status code
#         return "Request was not JSON", 400


@app.route("/json", methods=["POST"])
def json_example():
    if request.is_json:               # we are getting json first and sending it a response as json object
        req = request.get_json()    
        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")
        }
        res = make_response(jsonify(response_body), 200)
        return res
    else:
        # return make_response(jsonify({"message": "Request body must be JSON"}), 400) 
        response_body = {
            "message": "Request body must be JSON"
        }
        res = make_response(jsonify(response_body), 400)
        return res



# Flask & the Fetch API (AJAX?) - Python on the web - Learning Flask Series Pt. 10   ********************************
        
@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()     # Parse the incomming JSON  into a Python dictionary
    print( req)    # now  we have got a dictionary of {'name': 'Nouman', 'message': 'Test Msg'} our form we submit

    # res = make_response(jsonify({"message": "Json Received"}), 200)

    res = make_response(jsonify(req), 200)                               
    return res



# Flask query strings - Python on the web - Learning Flask Series Pt. 11        ********************************

# query string (set of key and value pairs like in https://www.google.com/search?q=quetry+string)
#
# syntax:
# write ? after path and give key and value pairs, separated by & .
#  as key=value&key=value
# 
# http://127.0.0.1:5000/query?foo=foo&bar=bar&baz=baz&title=query+strings+with+flask
# ImmutableMultiDict([('foo', 'foo'), ('bar', 'bar'), ('baz', 'baz'), ('title', 'query strings with flask')])

@app.route("/query")
def query():
    if request.args:    #  check if there any query strings
        args = request.args  #  request.args has parsed our query string and conveniently converted
                             #  it into an ImmutableMultiDict which we can treat just like a Python dictionary
        print(args)  
          
        
        # for k, v in args.items():    # we can iterate throught this dictionary
        #     print(f"{k}: {v}")

        if "foo" in args:           
            foo = args["foo"]     #  args.get("foo")
            print(foo)

        return "hello"
        
    else:
        return "No query string received", 200



