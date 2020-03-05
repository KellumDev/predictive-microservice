# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:49:51 2020

@author: mika.hlavin
"""


import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

import pandas as pd
from pandas.io.json import json_normalize

import json 
 
h2o.init()

rf = h2o.load_model(path="C:/Users/austin.kellum/Documents/Python_webservice/predictions/DRF_model_python_1583350791193_1")

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

'''
  quasAnswer = inst.getQuery(quesAsked)
            #formatAns = {"fulfillmentText": "This is a text response", 'fulfillmentMessages': [{'text': {'text': [quasAnswer]}}]}
            formatAns = {"fulfillmentText":quasAnswer}



'''
#unknown = ""C:\Users\austin.kellum\Documents\Python_webservice\wine_test_data.csv""
def run_init(unknown): #file path to excel
    #h2o.init
    
    # normalize 
    normalized = json_normalize(unknown)
    
    normalized = h2o.H2OFrame(normalized)
    
    prediction = rf.predict(normalized)
    prediction = prediction.as_data_frame(use_pandas=True)
    prediction = prediction['predict']
    prediction = prediction.to_list()
    pred_dict = {'prediction': prediction}
    prediction_json= json.dumps(pred_dict)
    #jsonify
    
    
    print("..done")
    #prediction=pd.DataFrame(prediction)
    #formatAns = {"prediction": prediction}
     #prediction = json.dumps(formatAns)
        
    
    return prediction_json 

#result = run_init(data_test)
#print(result)



#------------------------------- Need later -----------------------------------
     # prediction.to_json(orient='split')
    #formatAns = {"prediction": prediction}
#    prediction = unknown['prediction']= prediction['predict quality']
   # prediction.to_json(orient='split')
#------------------------------- Need later -----------------------------------
 