# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:31:16 2019

@author: Mahdi Rahbar
"""
import numpy as np
import joblib
from sklearn import svm

class InputClassifier:

    model = joblib.load('tc/model/SVCmodel.sav')

    def __init__(self, imported_data):
        self.imported_data = imported_data
    
    def SVCClassifier(self):
        return InputClassifier.model.predict(self.imported_data)