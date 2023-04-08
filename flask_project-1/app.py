#Step-1 importing
from flask import Flask
#Step-2 Create the object with a parameter __name__
app = Flask(__name__)

#Step-3 creating the endpoint using routes and bind them with a functionality
@app.route('/')
def Home():
    return "Hello World"

@app.route('/AboutUS')
def AboutUS():
    return ("Welcome")

#Step-4 run the application
if __name__ == '__main__':
    app.run()