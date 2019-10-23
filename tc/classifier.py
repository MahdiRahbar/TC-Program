# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:31:16 2019

@author: Mahdi Rahbar
"""
import numpy as np
import joblib
from sklearn import svm

class InputClassifier:

    model = joblib.load('./tc/model/SVCmodel_Proba.sav')
    labels = joblib.load('./tc/model/label_encoder.joblib')
    def __init__(self, imported_data):
        self.imported_data = imported_data
        self.Fin_Results = []
        self.clf_labels = ['انسانی','فنی','هنر','پایه','پزشکی']
    
    def Show_Label(self):
        le = InputClassifier.labels
        return list(le.inverse_transform(self.Fin_Results))

    def SVCClassifier(self):
        self.Fin_Results = InputClassifier.model.predict(self.imported_data)
        return self.Fin_Results 

    def SVC_Proba(self):
        return InputClassifier.model.predict_proba(self.imported_data)

    def Display_Proba(self):
        Proba_text = ''
        Proba_M = self.SVC_Proba()
        I , J = Proba_M.shape
        for i in range(I):
            Proba_text +='%d :  |  '%i 
            for j in range(J):
                Proba_text = Proba_text + self.clf_labels[j] + ": %.2f " % Proba_M[i,j] + '  |  '
            Proba_text += '\n'
        return Proba_text
