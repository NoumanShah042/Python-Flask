from flask import Flask, render_template, request, redirect, url_for, abort

# Initialize the Flask application
app = Flask(__name__)

"""
Flask Redirect and Errors

Flask class provides the redirect() function which redirects the user to some specified URL with
 the specified status code.

An HTTP status code is a response from the server to the request of the browser. 
When we visit a website, a request is sent to the server, and the server then responds to the 
browser's request with a three-digit code: the HTTP status code. 
This status code also represents the error.


"""

@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['txtemail'] == 'noumanrehman042@gmail.com' and \
            request.form['txtpass'] == '1234':
        return redirect(url_for('success'))
    else:
        abort(401)
    # else:
    #     return redirect(url_for('errorlogin'))


@app.route('/success')
def success():
    return '<h1>logged in successfully</h1>'


@app.route('/errorlogin')
def errorlogin():
    return '<h1>Bad Credentials. Please login again <a href = "/">login</a></h1>'


if __name__ == '__main__':
    app.run(debug=True)


"""
Errors

Standard HTTP Codes
The following HTTP codes are standardized.

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
The default status code is HTTP_302_FOUND.

The abort() function
The abort() function is used to handle the cases where the errors are involved in the requests from the client side, such as bad requests, unauthorized access and many more. However, the error code is to be mentioned due to which the error occurred.

The syntax to use the abort() function is given below.

Flask.abort(code) 

The Following error codes depending upon the specified errors.

400: for bad requests
401: for unauthorized access
403: for forbidden
404: for not found
406: for not acceptable
415: for unsupported media types
429: for too many requests
"""
