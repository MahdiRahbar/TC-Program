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

    # def Doc_Text_Convertor(self):
    #     # return text or save it 
    def Docx_Text_Convertor(self):
        # return text or save it 
        try:
            file_path = the_path+filename
            doc = docx.Document(file_path)
            temp_doc = []
            for i in doc.paragraphs:
                temp = i.text.split()
                for j in temp:
                    temp_doc.append(j)
            temp_doc = seperator.join(temp_doc)
            textfile_name=str(saving_path)+preFix+ str(filename[:-5]) + ".txt"

            with open(textfile_name, 'w',encoding='utf8') as f:
                for item in temp_doc:
                    f.write("%s" % item)    
        except:
            pass

    def Text_Maker_Save(self):
        path_string= self.path
        for filename in os.listdir(path_string):
            x1 = re.search("*.txt$", filename)
            x2 = re.search("*.docx$", filename)
            x3 = re.search("*.doc$", filename)
            if x1:
                pass
            elif(x2): 
                self.Docx_Text_Convertor()
            elif(x3):                
                print(filename," file will not be processed because its format is not\
                        accepted by this software. ( only accepts .txt and .docx )")


    