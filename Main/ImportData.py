# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:34:07 2019

@author: Mahdi Rahbar
"""

import docx 
import os 
import re

class DataImport:
    def __init__(self, path):
        self.path = path 
        self.keep_text = keep_text

    def Corpus_Reader(self):
        string_corpus = []
        set_class = ''
        for filename in os.listdir(self.path):
            file_path = self.path+filename
            loaded_file = open(file_path,'r',encoding = "utf-8") 
            line_seperated_data = loaded_file.readlines() 
            set_class = str(filename[:2])
            string_corpus.append([line_seperated_data[0],set_class])
        return string_corpus

class DocToText:
    def __init__(self, path, save_path, keep_text):
        self.path = path
        self.save_path = save_path
        self.keep_text = keep_text

    def Doc_Text_Convertor(self):
        # return text or save it 
    def Docx_Text_Convertor(self):
        # return text or save it 

    def Check_Text_Status(self):
        path_string= self.path
        x1 = re.search("*.txt$", path_string)
        x2 = re.search("*.doc$", path_string)
        x3 = re.search("*.docx$", path_string)

                

    