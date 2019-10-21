# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:41:54 2019

@author: Mahdi Rahbar
"""

import numpy as numpy
import pandas as pd
from hazm import *
import joblib
import re
from string import punctuation
from collections import OrderedDict
from collections import Counter, defaultdict
import collections
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer,\
                            TfidfTransformer, TfidfVectorizer


class PreProcessing: 
    def __init__(self, imported_data,stopwords_list):
        self.imported_data = imported_data
        self.stopwords_list = stopwords_list
    
    def TextCleaner(self):
        self.stopwordsList= ''
        Data = self.imported_data
        stemmer = Stemmer()
        lemmatizer = Lemmatizer()
        dataList = Data
        table = str.maketrans('', '', punctuation)
        for i in range(0, len(dataList)):
            vocabulary = []
            for j in range(0, len(dataList[i][0])):
                dataList[i][0][j] = stemmer.stem(dataList[i][0][j])
                dataList[i][0][j] = lemmatizer.lemmatize(dataList[i][0][j])
            dataList[i][0] = [word for word in dataList[i][0] if word.isalpha()]
            dataList[i][0] = [w.translate(table) for w in dataList[i][0]]
            dataList[i][0] = [word for word in dataList[i][0] if len(word) > 3]
            vocabulary.append(dataList[i])      
        return dataList

    def Data_Vectorizer(self):
        count_vect = joblib.load('model/Vec_Most_Frequence.sav')
        X_train_counts = count_vect.fit_transform(self.imported_data)
        X_train_counts.shape
        tf_transformer = joblib.load('model/Vec_TF_IDF.sav')
        X_train_tf = tf_transformer.transform(X_train_counts)
        return X_train_tf

    
