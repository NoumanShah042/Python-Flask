# https://pythonise.com/series/learning-flask/flask-uploading-files
# https://www.youtube.com/watch?v=6WruncSoCdI&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L&index=13

from app import app
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
import os

# cd app/static/img/uploads/
# D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\img\uploads

# app.config["IMAGE_UPLOADS"] ="D:/Python_ Flask programming/Julian Nash/APP templates Inheritance - 2/app/static/img/uploads"

app.config["IMAGE_UPLOADS"] = r"D:\Python_ Flask programming\Julian Nash\APP templates Inheritance - 2\app\static\img\uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024    # 524,288 bytes


def allowed_image(filename):
    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            if not allowed_image_filesize(request.cookies["filesize"]):
                print("File size exceeded maximum limit")
                return redirect(request.url)

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                # Pass it a filename and it will return a secure version of it.
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                print("Image saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("public/upload_image.html")


"""
# code without validating image
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"] 
            # Using request.files["image"], we're able to access the file from the form with the attribute name="image"

            # print(image)  # <FileStorage: 'example.png' ('image/png')>

            print(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            # image.save("C:/Users/Syed Numan Rehman/Desktop/"+ image.filename)
            # image.save(app.config["IMAGE_UPLOADS"]+ image.filename)

            print("Image saved")

            return redirect(request.url)


    return render_template("public/upload_image.html")

"""

"""
Securing file uploads
A user could upload any kind of file of any filesize, which is dangerous..

Tip - NEVER TRUST USER INPUT

To mitigate any damage our application might receive from a malicius actor 
 or user error, we should consider the following:

Ensuring the file has a name
Ensuring the file type is allowed
Ensuring the filename is allowed
Ensuring the filesize is allowed

"""
