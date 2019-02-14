# -*- coding: utf-8 -*-

import os
import requests
import random
import flask
import shutil
from flask import Flask
url = 'https://cdn.glitch.com/731b2b86-97c7-4581-83c3-cb37cd854060%2Fohueligrid.pdf?1529511144910'
response = requests.get(url, stream=True)
 #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
with open('ohueligrid.pdf', 'wb') as out_file:
  shutil.copyfileobj(response.raw, out_file)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=False)
    

    
    


