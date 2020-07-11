from flask import render_template # import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
from app import app # import the app instance from the app folder.
from .request import get_newsarticles #  import the get_newssources() function from the request module. We want to get the reuters newssource from our API.
import requests

@app.route('/') #  create a route decorator @app.route('/')
def index(): #define the view function index()
    r = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-11&sortBy=publishedAt&apiKey=5e261f0fb41047efaef7e64b3d40d5c4')
    response = r.json()
    return(r.json())
    return(response['status'])
    return(response['totalResults'])
    return(response['articles'])


@app.route('/newssource/<int:newssource_id>') #new route that has a newssource() view function. The part in the angle brackets <> is dynamic. And any route mapped to this will be passed. We changed the dynamic part to <int:newssource_id> to transform content to integer.
def newssource(newssource_id): # returns a response of a newssource.html file. By default, dynamic parts are rendered as strings but they can be transformed to be of any type
    
    return render_template('newssource.html',id = newssource_id) 

    