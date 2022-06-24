import requests

requests.get("https://www.google.com")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'