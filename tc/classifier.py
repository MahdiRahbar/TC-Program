# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:31:16 2019

@author: Mahdi Rahbar
"""
import numpy as np
import joblib
from sklearn import svm

class InputClassifier:

    model = joblib.load('./tc/model/SVCmodel.sav')
    labels = joblib.load('./tc/model/label_encoder.joblib')
    def __init__(self, imported_data):
        self.imported_data = imported_data
        self.Fin_Results = []
    
    def Show_Label(self):
        le = InputClassifier.labels
        return list(le.inverse_transform(self.Fin_Results))

    def SVCClassifier(self):
        self.Fin_Results = InputClassifier.model.predict(self.imported_data)
        return self.Fin_Results 
    def SVC_Proba(self):
        return InputClassifier.model.predict_proba(self.imported_data)