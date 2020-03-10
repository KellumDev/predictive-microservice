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

rf = h2o.load_model(path="C:/Users/austin.kellum/Documents/Python_webservice/predictions/drf_model_v3")

 
 
def run_init(unknown): #file path to excel
    #h2o.init
    
    # normalize 
    normalized = json_normalize(unknown)
    
    normalized = h2o.H2OFrame(normalized)
    prediction = rf.predict(normalized)
    prediction_pd = prediction.as_data_frame(use_pandas=True)
    prediction_pd = prediction_pd['predict']
    prediction_pd = prediction_pd.to_list()
    pred_dict = {'wine_quality_prediction': prediction_pd}
    prediction_json= json.dumps(pred_dict)
    
    #remove the normalized frame 
    # remove the prediction 
    print("..done")
  
    
    return prediction_json 

#result = run_init(data_test)
#print(result)


 