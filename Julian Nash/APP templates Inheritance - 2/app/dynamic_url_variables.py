
"""
Full list of variable rules:   //  dynamic urls

Converter	Function
string  	Accepts any text without a slash (Default)
int     	Accepts positive integers  (  123 )
float	    Accepts positive floating point values  ( 123.89)
path	    Like string but also accepts slashes  ( img/image.png )
uuid	    Accepts UUID strings (Universally unique identifier) (e.g 118bc9c3-1af4-4d46-87a1-266db2e64e7a)


By default type is string ( in case if we do not specify)
If type of variable is not same in the url , browser will throw an error.

Using any of the converters listed above will convert the incoming variable into it's related type.
For example, if you define a url with <int:some_integer>, Flask will try to convert it into an integer, 
<path:path_to_some_file> will allow a path like string, including slashes etc..

"""

from app import app

@app.route("/variable/<string:var_name>")
def testing_url(var_name):
    print(var_name)
    print(type(var_name))
    # return str(var_name)
    return  {"name":"nouman"}
    
    
# The return type must be a string, dict, tuple, Response instance,
#  or WSGI callable, but it was a int.