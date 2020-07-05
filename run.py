from app import app # import app instance

if __name__ == '__main__': #check if script is run directly 
    app.run() # app.run () method to launch server, remove the debug = True argument from our app.run() because the debug mode has been enabled in the configuration file. (debug mode on to track errors)