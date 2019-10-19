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

    def Text_Maker(self):
        path_string= self.path
        x1 = re.search("*.txt$", path_string)
        x2 = re.search("*.doc$", path_string)
        x3 = re.search("*.docx$", path_string)
        if x1 or x2 or x3: 
            if x1:
                pass
            elif(x2): 
                Doc_Text_Convertor(self)
            elif(x3)
                Docx_Text_Convertor(self)
        else: 
            for filename in os.listdir(path_string):
                x1 = re.search("*.txt$", filename)
                x2 = re.search("*.doc$", filename)
                x3 = re.search("*.docx$", filename)
                if x1:
                    pass
                elif(x2): 
                    Doc_Text_Convertor(self)
                elif(x3)
                    Docx_Text_Convertor(self)
                

    