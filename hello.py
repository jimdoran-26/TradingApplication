from flask import Flask
from get_data import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'