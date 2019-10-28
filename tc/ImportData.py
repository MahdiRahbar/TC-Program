# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:34:07 2019

@author: Mahdi Rahbar
"""
import ntpath
import docx 
import os 
import re
from os.path import splitext, split


class Data_Reader:
    '''
    Data_Reader Class: 
    '''
    def __init__(self, path, save_path, keep_text):
        self.path = path
        self.save_path = save_path
        self.keep_text = keep_text
        self.doc_names =  []


    def Corpus_Reader(self):
        string_corpus = []
        set_class = ''
        
        for filename in os.listdir(self.path):
            f_name , f_ext = splitext(filename)  
            if f_ext==".txt":
                self.doc_names.append(f_name)
                file_path = self.path+'/'+filename
                loaded_file = open(file_path,'r',encoding = "utf-8") 
                line_seperated_data = loaded_file.readlines() 
                set_class = str(filename[:2])
                string_corpus.append([line_seperated_data[0],set_class])
 
        return string_corpus, self.doc_names
    



    def Docx_Text_Convertor(self,file_path): 

        saving_path = self.path+'/'   # it must change in future.
        
        preFix= ''
        seperator=' '  
        temp=''
        file_name_ = ntpath.basename(file_path)
        file_name_wF, f_ext = splitext(file_name_)
        print(file_path)
        try:            
            doc = docx.Document(file_path)
            temp_doc = []
            for i in doc.paragraphs:
                temp = i.text.split()
                for j in temp:
                    temp_doc.append(j)
            temp_doc = seperator.join(temp_doc)
            textfile_name=str(saving_path)+preFix+ file_name_wF + ".txt"
            with open(textfile_name, 'w',encoding='utf8') as f:
                for item in temp_doc:
                    f.write("%s" % item)    
        except:
            raise

    def Text_Maker_Save(self):
        path_string= self.path

        for filename in os.listdir(path_string):
            _ , f_ext = splitext(filename)
            if (f_ext == '.txt'):
                pass

            elif(f_ext == '.docx'): 
                self.Docx_Text_Convertor(path_string+"/"+filename)
            else:                
                print(filename," file will not be processed because its format is not accepted by this software. ( only accepts .txt and .docx )")



    def Save_Text_File(self):
        if self.keep_text: 
            pass

