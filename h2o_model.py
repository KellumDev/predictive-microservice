# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:22:02 2020

@author: mika.hlavin
"""

import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

h2o.init()

train = h2o.import_file(path = 'C:/Users/mika.hlavin/Desktop/wine_train_data.csv')
val = h2o.import_file(path = 'C:/Users/mika.hlavin/Desktop/wine_val_data.csv')

x = train.columns
y = 'quality'
x.remove(y)

rf = H2ORandomForestEstimator(seed = -1, ntrees = 50)
rf.train(x=x, y=y, training_frame=train)
model_path = h2o.save_model(model=rf, path="C:/Users/mika.hlavin/Desktop/wine_model", force=True)