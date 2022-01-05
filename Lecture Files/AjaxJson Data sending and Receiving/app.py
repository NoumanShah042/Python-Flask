from flask import Flask,request, render_template , session ,make_response , jsonify
from DBHandler import DBHandler
import datetime
abc = Flask(__name__)
abc.config.from_object('config')
#abc.secret_key = abc.config["SECRET_KEY"]
abc.secret_key = "gfsjhfg-87t678564786"


@abc.route('/testAjaxDatasending')
def testAjaxDatasending():
    return render_template("SendingJsontoServer.html")

@abc.route('/fetchData', methods=['POST'])
def getRandomeData():
    json_data = request.get_json()
    data_value=json_data["data"]
    d= datetime.datetime.now()
    datestring=d.strftime("%d-%M-%Y %H:%M:%S")
    value = data_value+datestring
    responseData={}
    responseData["responseData"]=value;
    return jsonify(responseData)



@abc.route('/')
def hello_world():
    return render_template("login.html")
def test():
    return "My Hello"
abc.add_url_rule("/test","tt",test)


@abc.route("/signin", methods=["POST"])
def signin():
    error = None
    db = None
    try:
        print("Signin")
        email = request.form['email']
        password = request.form['password']
        #session["email"]=email
        #session["password"]=password
        #session["email"] = email
        # print(session["fname"])
        print(abc.config["DATABASEIP"])
        db = DBHandler(abc.config["DATABASEIP"], abc.config["DB_USER"], abc.config["DB_PASSWORD"],
                       abc.config["DATABASE"])
        signin = db.signin(email, password)
        if signin:
            print("successful login")
            #return render_template('dashboard.html', email=email)
            response = make_response(render_template("dashboard.html",email=email))
            response.set_cookie("userEmail",email ,max_age=60   )
            print("created cookie")
            response.set_cookie("test","123",max_age=60)
            return response
        else:
            return render_template('login.html', error="Login failed Invalid username or password")

    except Exception as e:
        print(e)
        error = str(e)
        print(error)
        return render_template('login.html', error="Login failed Invalid username or password")


@abc.route('/showcourses')
def showcourses():
    db = DBHandler(abc.config["DATABASEIP"], abc.config["DB_USER"], abc.config["DB_PASSWORD"], abc.config["DATABASE"])
    #email=request.cookies.get("email")
    #print(session["email"])
    #email = request.cookies.get("userEmail")
    #if session.get("email"):
    if request.cookies.get("userEmail"):
        courses=db.showCourses(request.cookies.get("userEmail"))
        #return render_template("showCourses.html" ,email=session["email"],courses=courses)
        return render_template("showCourses.html", email=request.cookies.get("userEmail"), courses=courses)
    else :
        return render_template("showCourses.html" )

@abc.route('/home')
def home():
    if session.get("email") !=None:
        return render_template("dashboard.html" , email=session['email'])
    else:
        return render_template("login.html", email=None)
@abc.route('/logout')
def logout():
    session.clear()
    print("in logout function")
    return render_template("login.html")


@abc.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    db = None
    try:
        print("Test")
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        #session["email"]=email
        #session["fname"]=fname

        #print(session["fname"])
        print(abc.config["DATABASEIP"])
        db = DBHandler(abc.config["DATABASEIP"],abc.config["DB_USER"],abc.config["DB_PASSWORD"],abc.config["DATABASE"])
        d = db.signup(email,password,fname,lname)
        response = make_response(render_template('dashboard.html' , email=email ))
        response.set_cookie("userEmail",email)
        response.set_cookie("test","123")
        return response
        #return render_template('dashboard.html' , email=email )

    except Exception as e:
        print(e)
        error = str(e)
        return render_template('login.html', error=error)




if __name__ == '__main__':
    abc.run()
