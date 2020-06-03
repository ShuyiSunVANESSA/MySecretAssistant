# Import the framework
from flask import Flask
import os

# Create and instance of Flask
app = Flask (__name__)

@app.route("/")
def index():
    return "aloha!"