from flask import Flask
# class Flask(_PackageBoundObject):   in following file
# C:\Users\Syed Numan Rehman\AppData\Local\Programs\Python\Python39\lib\site-packages\flask\app.py
# Flask is a class 
# we are making object of Flask class 

app = Flask(__name__)  


from app import views
from app import admin_views