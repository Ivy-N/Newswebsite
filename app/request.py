from app import app #  import the flask application instance.
import urllib.request,json #  import the Python urllib.request module that will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import newssource

Newssource = newssource.Newssource

api_key = app.config['NEWSSOURCE_API_KEY'] # access our app configuration objects by calling app.config['name_of_object']. We get the API key and the newssource URL. from app instance we get the API key from the config object.

base_url = app.config["NEWSSOURCE_API_BASE_URL"] 

def get_newssources(category): # Function that gets the json response to our url request,  takes in a news source category as an argument.

    get_newssources_url = base_url.format(category,api_key) #use the .format() method on the base_url and pass in the news source category and the api_key. This will replace the {} curly brace placeholders in the base_url with the category and api_key respectively. This creates get_newssources_url as the final URL for our API request.



    with urllib.request.urlopen(get_newssources_url) as url: #use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_newssources_url as an argument and sends a request as url

        get_newssources_data = url.read() # use the read() function to read the response and store it in a get_newssources_datavariable.
        get_newssources_response = json.loads(get_newssources_data) # convert the JSON response to a Python dictionary using json.loads function and pass in the get_newssources_data variable.
# if the response contains any data, we call a process_results() function that takes in the list of dictionary objects and returns a list of newssources objects. We then return newssource_results which is a list of newssource objects.

        newssource_results = None

        if get_newssources_response['results']:
            newssource_results_list = get_newssources_response['results']
            newssource_results = process_results(newssource_results_list)


    return newssource_results
