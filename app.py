#enter "flask run" in command line.
#server will start on port 5000.
#restart the server after each save.

from flask import Flask

app = Flask(__name__)

#this will dipslay at the home screen
@app.route("/")
def index():
    return "Welcome to the index page!"

#this will display at the /Jasmine/ route
@app.route("/Jasmine/")
def jasmine():
    return "My dog's name is Jasmine. What's your dog's name?"


#this will display at the /dog/<dogname>/ route
@app.route("/dog/<dogname>/")
def yourdog(dogname):
    return f"Your dog's name is {dogname}."



