# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:31:03 2020

@author: austin.kellum
"""

import flask
from flask import request , jsonify

import run_h2o as h2o_init

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data_test = [
    {'fixed_acidity': 0,
     'volatile_acidity': 0,
     'citric_acidity': 0,
     'residual_sugar': 0,
     'chlorides': 0,
     'free_sulfur_dioxide': 0,
     'total_sulfur_dioxide': 0,
     'density': 0,
     'pH': 0,
     'sulphates': 0,
     'alcohol': 0
     }
]

#------------------------------------------ Routes ---------------------------------# 
# input route for model 
@app.route('/api/hto/arb/', methods=['GET', 'POST'])
def api_serve_model(): 
    if request.method == 'POST':
        req_data = request.get_json() 
      #  result = h2o_init.run_init(req_data)
        return result
   
#home page of the application 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Mantis</h1><p>This site is a prototype API for Mantis.</p>"

#error handling the application
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Check again, the resource could not be found.</p>", 404


app.run()