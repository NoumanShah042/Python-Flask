from app import app
from flask import render_template, request, redirect, abort

"""
Errors Handling  ensures our users aren't confused when something goes wrong, 
also giving them a way to get home or back to the content.

Flask provides us with a simple way to throw and catch errors, along with 
displaying a custom HTML template for each error. When an HTTP error is raised,
for example a 404 Not Found or 500 Internal Server Error, we can catch it, 
handle it and return something relevant to the exception.

"""

@app.route('/error')
def custom_error():
    #     manually throw an error
    abort(404)  # Not found
    abort(405)  # Method Not allowed
    abort(500)  # Internal Server Error
    return "custom_error"

"""
Custom error handlers
Just as we can throw errors on demand, we can handle them using the errorhandler() decorator 
and attaching it to our app instance.

The syntax for a custom error handler:

@app.errorhandler(STATUS_CODE)
def function_name(error):

    # Do something here..
    # Log the error..
    # Send en email..
    # Etc ..

    return render_template("handler.html"), STATUS_CODE

"""

@app.errorhandler(404)
def not_found(e):
    return render_template("public/404.html")
    # if we enter the path that does not exist 
    # this function will be called 
    # example:
    # http://127.0.0.1:5000/gdgdhhd


@app.errorhandler(500)
def server_error(e):
    # to test it, call custom error in any route like
    # abort(500)
    # and go to that root  

    # email_admin(message="Server error", url=request.url, error=e)
    app.logger.info(f"Server Error: {e} \nRoute: {request.url}" )
    return render_template("public/500.html")
     

@app.route('/custom_server_error')
def custom_server_error():
   abort(500)