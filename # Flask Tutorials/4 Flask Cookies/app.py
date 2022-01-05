from flask import Flask, render_template, request, make_response

app = Flask(__name__)

"""
Flask – Cookies
A cookie is stored on a client’s computer in the form of a text file. Its purpose is to remember 
and track data pertaining to a client’s usage for better visitor experience and site statistics. 
In Flask, cookies are set on response object. 
Use make_response() function to get response object from return value of a view function.
 After that, use the set_cookie() function of response object to store a cookie. 
 Reading back a cookie is easy. The get() method of request.cookies attribute is used to read a cookie.
"""


@app.route('/')  # http://localhost:5000/
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])  # http://localhost:5000/setcookie
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')  # http://localhost:5000/getcookie
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)
