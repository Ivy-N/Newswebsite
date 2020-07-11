from app import app #  import the flask application instance.
import urllib.request,json #  import the Python urllib.request module that will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import newssource
import requests

Newssource = newssource.Newssource

api_key = app.config['NEWSSOURCE_API_KEY'] # access our app configuration objects by calling app.config['name_of_object']. We get the API key and the newssource URL. from app instance we get the API key from the config object.

base_url = app.config["NEWSSOURCE_API_BASE_URL"] 

def get_newsarticles():

    r = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-11&sortBy=publishedAt&apiKey=5e261f0fb41047efaef7e64b3d40d5c4')
    response = r.json()
    return(r.json())
    return(response['status'])
    return(response['totalResults'])
    return(response['articles'])
    # print(response['articles']['source'])
    # # print(response['articles']['author'])
    # # print(response['articles']['title'])
    # # print(response['articles']['description'])
    # # print(response['articles']['url'])
    # # print(response['articles']['urlToImage'])
    # # print(response['articles']['publishedAt'])
    # # print(response['articles']['content'])



# def get_newssources(category): # Function that gets the json response to our url request,  takes in a news source category as an argument.

#     get_newssources_url = base_url.format(category,api_key) #use the .format() method on the base_url and pass in the news source category and the api_key. This will replace the {} curly brace placeholders in the base_url with the category and api_key respectively. This creates get_newssources_url as the final URL for our API request.



#     with urllib.request.urlopen(get_newssources_url) as url: #use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_newssources_url as an argument and sends a request as url

#         get_newssources_data = url.read() # use the read() function to read the response and store it in a get_newssources_datavariable.
#         get_newssources_response = json.loads(get_newssources_data) # convert the JSON response to a Python dictionary using json.loads function and pass in the get_newssources_data variable.
# # if the response contains any data, we call a process_results() function that takes in the list of dictionary objects and returns a list of newssources objects. We then return newssource_results which is a list of newssource objects.

#         newssource_results = None

#         if get_newssources_response['results']:
#             newssource_results_list = get_newssources_response['results']
#             newssource_results = process_results(newssource_results_list)


#     return newssource_results

# def process_results(newssource_list): # Function  that processes the newssource result and transform them to a list of Objects. We create a function process_results() that takes in a list of dictionaries. We create an empty list newssource_results this is where we will store our newly created newssource objects.

#     newssource_results = []
#     for newssource_item in newssource_list: #  loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values.
#         id = newssource_item.get('id')
#         title = newssource_item.get('title')
#         description = newssource_item.get('description')
#         urlToImage = newssource_item.get('urlToImage_path')
#         publishedAt = newssource_item.get('publishedAt')
#         url = newssource_item.get('url')

#         if urlToImage: # Some newssource_item 's might not have a poster. This will give an error when we are trying to create an object. So we check if the newssource_item has a poster  
#             newssource_object = Newssource(id,title,description,urlToImage,publishedAt,url) ##we create the newssource object.
#             newssource_results.append(newssource_object) # We use the values we get to create a new newssource object then we append it to our empty list.

#     return newssource_results #  We then return the list with newssource objects.



