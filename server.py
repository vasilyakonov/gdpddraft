# -*- coding: utf-8 -*-

import os
import requests
import random
import flask
import shutil
import bs4
from flask import Flask

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
    

from bs4 import BeautifulSoup 

# load the file
with open("./templates/about.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
soup.head.append(new_link)

# save the file again
with open("./templates/about.html", "w") as outf:
    outf.write(str(soup))
    print(soup.prettify())
    
    


    
    


