
from crypt import methods
from flask import Flask

app = Flask('assignment2')

@app.route("/", methods=["GET"])
def home():
    return "This is the home page"

@app.route("/about")
def about():
    me = {
        "first":"Alexis",
        "last":"Aldrete",
        "age": 25
    }
    return "<h2>Alexis Aldrete</h2>"

app.run(debug=True)