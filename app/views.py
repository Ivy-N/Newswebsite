from flask import render_template # import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
from app import app # import the app instance from the app folder.
from .request import get_newsources #  import the get_newssources() function from the request module. We want to get the popular newssource from our API.

@app.route('/') #  create a route decorator @app.route('/')
def index(): #define the view function index()
    popular_newssources = get_newssources('popular') # We create a variable popular_newssources where we call our get_newssources() function and pass in "popular" as an argument. we then pass the result from that function call to our template
    print(popular_newssources)
    title = 'Home - Welcome to The best News Source Website Online' #add a title variable
    return render_template('index.html', title = title,popular = popular_newssources) #use the render_template() function and pass in index.html file and title variable as argument. The first title on the left of the = sign, represents the variable in the template. While the one to the right represents the variable in our view function. We want to pass in a title to our templates instead of defining them inside the html structure. We create a variable title and pass it into our templates.

from .request import get_newssources

@app.route('/newssource/<int:newssource_id>') #new route that has a newssource() view function. The part in the angle brackets <> is dynamic. And any route mapped to this will be passed. We changed the dynamic part to <int:newssource_id> to transform content to integer.
def newssource(newssource_id): # returns a response of a newssource.html file. By default, dynamic parts are rendered as strings but they can be transformed to be of any type

    return render_template('newssource.html',id = newssource_id) 
