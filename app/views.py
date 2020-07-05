from flask import render_template # import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
from app import app # import the app instance from the app folder.


@app.route('/') #  create a route decorator @app.route('/')
def index(): #define the view function index()

    return render_template('index.html') # use the render_template() function and pass in index.html file