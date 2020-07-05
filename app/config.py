class Config: #The parent Config class contains configurations that are used in both production and development stages. 
    
    pass

class ProdConfig(Config): #  The ProdConfigsubclass contains configurations that are used in production stages of our application and inherits from the parent Config class.

    pass


class DevConfig(Config): # The DevConfig subclass contains configurations that are used in development stages of our application and inherits from the parent Config class.

    DEBUG = True # Inside DevConfig subclass, we add DEBUG = True; this enables debug mode in our application.