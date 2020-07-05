from flask import Flask # import Flask class from flask module
from .config import DevConfig # import our DevConfig subclass in our __init__.py file

app = Flask(__name__,instance_relative_config = True) #use Flask class to create app instance. Pass in the __name__ variable. Pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created.

app.config.from_object(DevConfig) #use app.config.from_object() method to set up configuration and pass in the DevConfig subclass.
app.config.from_pyfile('config.py') #The app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config.

from app import views #import our views file from the app folder in order to create views