# -*- coding: utf-8 -*-

import os
import requests
import random
import flask
from flask import Flask


from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"
if __name__ == '__main__':
    app.run(debug=True)


