class Config: #The parent Config class contains configurations that are used in both production and development stages. 
    
    NEWSSOURCE_API_BASE_URL ='https://api.newsapi.org//{}?api_key={}' # store the news source base URL inside the app/config file. We use the {} to represent sections in the URL that will be replaced with actual values


class ProdConfig(Config): #  The ProdConfigsubclass contains configurations that are used in production stages of our application and inherits from the parent Config class.

    pass


class DevConfig(Config): # The DevConfig subclass contains configurations that are used in development stages of our application and inherits from the parent Config class.

    DEBUG = True # Inside DevConfig subclass, we add DEBUG = True; this enables debug mode in our application.