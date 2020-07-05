from flask import Flask # import Flask class from flask module
from .config import DevConfig # import our DevConfig subclass in our __init__.py file

app = Flask(__name__) #use Flask class to create app instance. Pass in the __name__ variable

app.config.from_object(DevConfig) #use app.config.from_object() method to set up configuration and pass in the DevConfig subclass.

from app import views #import our views file from the app folder in order to create views