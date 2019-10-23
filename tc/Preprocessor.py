# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:41:54 2019

@author: Mahdi Rahbar
"""

import numpy as numpy
import pandas as pd
from hazm import *
import pickle
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
        self.stringList=[]
    
    def TextCleaner(self):
        self.stopwordsList= ''
        Data = self.imported_data
        stemmer = Stemmer()
        lemmatizer = Lemmatizer()
        dataList = Data
        table = str.maketrans('', '', punctuation)
        for i in range(0, len(dataList)):
            for j in range(0, len(dataList[i][0])):
                dataList[i][0][j] = stemmer.stem(dataList[i][0][j])                
                dataList[i][0][j] = lemmatizer.lemmatize(dataList[i][0][j])
            dataList[i][0] = [word for word in dataList[i][0] if word.isalpha()]
            dataList[i][0]= [w.translate(table) for w in dataList[i][0]]
            dataList[i][0] = [word for word in dataList[i][0] if len(word) > 3]
        self.imported_data = dataList
        return self.imported_data

    def String_Splitter(self):
        # print(type(self.imported_data[0][0][23]))
        for i in range(len(self.imported_data)):
            self.imported_data[i][0]=self.imported_data[i][0].split()
        return self.imported_data

    def wordToString(self):
        self.stringList = []
        for i in range(0,len(self.imported_data)):
            self.stringList.append(' '.join(word for word in self.imported_data[i][0]))
        self.imported_data = self.stringList
        return self.imported_data

    def Data_Vectorizer(self):
        # count_vect = joblib.load('./tc/model/Vec_Most_Frequence.sav')
        count_vect = CountVectorizer(decode_error="replace",\
                                    vocabulary=pickle.load(open("./tc/model/count_vect.pkl", "rb")))  # count_vect.pkl
        X_train_counts = count_vect.fit_transform(self.imported_data)
        # print(X_train_counts.shape)
        tf_transformer = TfidfTransformer().fit(X_train_counts) # use_idf=False
        X_train_tf = tf_transformer.transform(X_train_counts)
        # print(X_train_counts.shape)

        return X_train_tf

    
