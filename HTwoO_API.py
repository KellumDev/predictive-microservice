# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:31:03 2020

@author: austin.kellum
"""

import flask
from flask import request , jsonify

import modeltest

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data_test = [
    {'fixed_acidity': 0,
     'volatile_acidity': 'A Fire Upon the Deep',
     'citric_acidity': 'Vernor Vinge',
     'residual_sugar': 'The coldsleep itself was dreamless.',
     'chlorides': 'The coldsleep itself was dreamless.',
     'free_sulfur_dioxide': 'The coldsleep itself was dreamless.',
     'total_sulfur_dioxide': 'The coldsleep itself was dreamless.',
     'density': 'The coldsleep itself was dreamless.',
     'pH': 'The coldsleep itself was dreamless.',
     'sulphates': 'The coldsleep itself was dreamless.',
     'alcohol': 'The coldsleep itself was dreamless.'
     }
]

#------------------------------------------ Routes ---------------------------------
#home page of the application 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Mantis</h1><p>This site is a prototype API for Mantis.</p>"

#error handling the application
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Check again, the resource could not be found.</p>", 404

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(data_test)

#allow user to use input and post to the application 
@app.route('/api/hto/arb/', methods=['GET', 'POST'])
def api_by_id(): 
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    # create an empty list for results
    results = []
    
    for book in books: 
        if book['id'] == id: 
            results.append(book)
    
    return jsonify(results)
 
                    
app.run()