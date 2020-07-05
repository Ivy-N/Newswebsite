from flask import render_template # import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
from app import app # import the app instance from the app folder.


@app.route('/') #  create a route decorator @app.route('/')
def index(): #define the view function index()
 
    message = 'Hello World' #add a message variable
    return render_template('index.html',message = message) #use the render_template() function and pass in index.html file and message variable as argument. The first message on the left of the = sign, represents the variable in the template. While the one to the right represents the variable in our view function.

@app.route('/newssource/<int:newssource_id>') #new route that has a newssource() view function. The part in the angle brackets <> is dynamic. And any route mapped to this will be passed. We changed the dynamic part to <int:newssource_id> to transform content to integer.
def newssource(newssource_id): # returns a response of a newssource.html file. By default, dynamic parts are rendered as strings but they can be transformed to be of any type

    return render_template('newssource.html',id = newssource_id) 