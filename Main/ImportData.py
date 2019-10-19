# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:34:07 2019

@author: Mahdi
"""

import docx 
import os 

def corpus_reader(the_path,):
    string_corpus = []
    the_path = the_path
    set_class = ''
    for filename in os.listdir(the_path):
        file_path = the_path+filename
        loaded_file = open(file_path,'r',encoding = "utf-8") 
        line_seperated_data = loaded_file.readlines() 
        set_class = str(filename[:2])
        string_corpus.append([line_seperated_data[0],set_class])
    return string_corpus