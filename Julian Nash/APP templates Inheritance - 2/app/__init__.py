from flask import Flask

app = Flask(__name__)

# *********************
# setting up a config file
# app.config.from_object("config_filename.ConfigClass")  #  syntax
# app.config.from_object("config.DevelopmentConfig")      # example

# *********************
# Loading a config file (dynamically)
# if app.config["ENV"] == "production":
#     app.config.from_object("config.ProductionConfig")
# else:
#     app.config.from_object("config.DevelopmentConfig")
# *********************

# print(f'ENV is set to: {app.config["ENV"]}')

# *********************

# importing my modules
from app import views
from app import admin_views
from app import cookies_
from app import session_object
from app import uploading_files
from app import sending_files
from app import dynamic_url_variables
from app import message_flashing_and_notifications
from app import error_handler


