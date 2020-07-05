from app import app # import app instance

if __name__ == '__main__': #check if script is run directly 
    app.run(debug = True) # app.run () method to launch server, debug mode on to track errors