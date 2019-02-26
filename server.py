# -*- coding: utf-8 -*-
import os
import requests
import random
import flask
import shutil
import bs4
import jinja2
import subprocess
import json

from flask import Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')
  
@app.route('/calendar')
def calendar():
     return render_template('calendar.html')
  
@app.route('/typefaces')
def typefaces():
     return render_template('typefaces.html')
  
@app.route('/lugemik')
def lugemik():
     return render_template('lugemik.html')
  
@app.route('/imposter')
def imposter():
     return render_template('imposter.html')

@app.route('/hypergraphx')
def hypergraphx():
     return render_template('hypergraphx.html')
  
if __name__ == '__main__':
    app.run(debug=False)
  
  
ubprocess.call("refresh") 




