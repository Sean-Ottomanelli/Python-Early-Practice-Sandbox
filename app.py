from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page!"

@app.route("/Jasmine/")
def jasmine():
    return "My dog's name is Jasmine. What's your dog's name?"

@app.route("/<dogname>/")
def yourdog(dogname):
    return f"Your dog's name is {dogname}."



