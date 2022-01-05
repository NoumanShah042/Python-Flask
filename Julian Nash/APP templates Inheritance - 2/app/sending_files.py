from app import app
from flask import render_template, request, redirect
from flask import send_file, send_from_directory, safe_join, abort

# https://www.youtube.com/watch?v=QjpbWAirMWw&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L&index=14
# https://pythonise.com/series/learning-flask/sending-files-with-flask

# from flask import send_file, send_from_directory, safe_join, abort
# send_file                 allows us to send the contents of a file to the client
# send_from_directory       allows us to send a specific file from a directory (Recommended)
# safe_join                 allows us to safely join a filename with a file/directory path
# abort                     allows us to abort a request and return an HTTP status code of our choosing



# The absolute path of the directory containing images for users to download

app.config["CLIENT_IMAGES"] =  r"D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\client\img"

# The absolute path of the directory containing CSV files for users to download
app.config["CLIENT_CSV"] = r"D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\client\csv"

# The absolute path of the directory containing PDF files for users to download
app.config["CLIENT_PDF"] = r"D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\client\pdf"

# The absolute path of the directory containing PDF files for users to download
app.config["CLIENT_REPORTS"] = r"D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\client\reports"


@app.route("/get-files")
def helpClient():
    return """
    <h3 style='color: green;'>

    <a href="http://127.0.0.1:5000/get-image/002.jpg">Click to download image</a><br>
    http://127.0.0.1:5000/get-image/002.jpg    <br>
    http://127.0.0.1:5000/get-csv/data.csv     <br>
    http://127.0.0.1:5000/get-image/get-report/2017/jan/download.txt      <br>   
    http://127.0.0.1:5000/send-csv/data.csv
       
            
    </h3>
    """


# as_attachment= False   -->   only show the file
# as_attachment= True    -->   automatically download the file

# *********************************

# http://127.0.0.1:5000/get-image/002.jpg
@app.route("/get-image/<image_name>")
def get_image(image_name):

    try:
        return send_from_directory(app.config["CLIENT_IMAGES"],  filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# *********************************

# http://127.0.0.1:5000/get-csv/data.csv
@app.route("/get-csv/<filename>")
def get_csv(filename):

    try:
        return send_from_directory(app.config["CLIENT_CSV"], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# *********************************

# http://127.0.0.1:5000/get-image/get-report/2017/jan/download.txt
@app.route("/get-report/<path:path>")
def get_report(path):

    try:
        return send_from_directory(app.config["CLIENT_REPORTS"], filename=path, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# *********************************

@app.route("/send-csv/<path:filename>")
def send_csv(filename):

    safe_path = safe_join(app.config["CLIENT_CSV"], filename)

    try:
        return send_file(safe_path, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# *********************************

"""
send_from_directory function arguments:

app.config["CLIENT_IMAGES"] - The path to the directory containing the images we're allowing our users to download
filename=image_name -        The image_name variable passed in from the URL
as_attachment=True -         Allows the client to download the file as an attachment
send_from_directory          is then returned the file

"""

# *********************************
