# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:18:22 2020

@author: austin.kellum
"""

import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

class h2oModel():
    
     def __init__(self, unknown, prediction):
        self.unknown = unknown
        self.prediction = prediction
        
        
    #import the json data 
    train = h2o.import_file( )
    
    x = train.columns
    y = 'quality'
    x.remove(y)

    rf = H2ORandomForestEstimator(seed = -1, ntrees = 50)
    rf.train(x=x, y=y, training_frame=train)