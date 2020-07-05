from flask import Flask #import Flask class from flask module

app = Flask(__name__) #use Flask class to create app instance. Pass in the __name__ variable

from app import views #import our views file from the app folder in order to create views