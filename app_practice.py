from cProfile import run
from unicodedata import name

# Import Flask
from flask import Flask

# Create an app
app = Flask(__name__)

# Define Index Route
@app.route('/')
def __hello_world__():
    return 'Hello World'

# Define the about route
@app.route('/about')
def about():
    return 'This is my about page'





# ----------------------------
# On Powershell run:
# set FLASK_APP=app.py
# Followed by:
# flask run
# ---------------------------- 