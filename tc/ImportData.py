# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:34:07 2019

@author: Mahdi Rahbar
"""

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

    # def Doc_Text_Convertor(self):
    #     # return text or save it 

    def Corpus_Reader(self):
        string_corpus = []
        set_class = ''
        for filename in os.listdir(self.path):
            if re.search(".txt$", filename):
                file_path = self.path+'/'+filename
                loaded_file = open(file_path,'r',encoding = "utf-8") 
                line_seperated_data = loaded_file.readlines() 
                set_class = str(filename[:2])
                string_corpus.append([line_seperated_data[0],set_class])
        return string_corpus


    def Docx_Text_Convertor(self,file_path): 
        # return text or save it      
        saving_path =self.save_path 
        preFix= ''
        my_seperator=' '  
        try:            
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
            _ , f_ext = splitext(filename)
            if (f_ext == '.txt'):
                pass

            elif(f_ext == '.docx'): 
                self.Docx_Text_Convertor(path_string+filename)

            else:                
                print(filename," file will not be processed because its format is not accepted by this software. ( only accepts .txt and .docx )")





class DataReader():
    """
    It handels data-related tasks like reading, etc.
    Parameters
    ----------
    file_path : str
        Path to the dataset file.
    sep : str
        Separator character
    header : boolean
        whether the dataset has header names or not.
    Attributes
    ----------
    X_train : array-like, shape (n_samples, n_features)
        Training samples in NumPy array.
    y_train :  array-like, shape(n_samples,)
        Class labels of training samples.
    hdr_names : list
        Header names of datasets.
    filename : str
        dataset's filename
    """

    def __init__(self, file_path, sep, header):

        self.file_path = file_path
        self.sep = sep
        self.header = header

    def load_data(self, shuffle, normalize):
        """
        It reads a CSV file into pandas DataFrame.
        Parameters
        ----------
        shuffle : boolean
            Whether to shuffle the dataset or not.
        normalize : boolean
            Whether to normalize the dataset or not.
        """

        f_name, f_ext = splitext(self.file_path)

        if f_ext == '.txt':

            df = pd.read_csv(self.file_path, sep=self.sep)
            self.hdr_names = list(df.columns.values)[1:] if self.header else []

        elif f_ext == '.libsvm':

            X, y, _ = read_libsvm(self.file_path)

            df = pd.DataFrame(np.hstack((y.reshape(X.shape[0], 1), X)))
            self.hdr_names = []
            
            # Check that the lables of binary problems are +1 and -1.
            class_label = df.iloc[:, 0].unique()
            
            if class_label.size == 2:
                
                if not(1 in class_label and -1 in class_label):
                    
                    df.iloc[:, 0][df.iloc[:, 0] == class_label[0]] = 1 
                    df.iloc[:, 0][df.iloc[:, 0] == class_label[1]] = -1 

        else:

            raise ValueError("Dataset format is not supported: %s" % f_ext)

        if shuffle:

            df = df.sample(frac=1).reset_index(drop=True)

            # print(df)

        # extract class labels
        self.y_train = df.iloc[:, 0].values
        df.drop(df.columns[0], axis=1, inplace=True)

        if normalize:

            df = (df - df.mean()) / df.std()

        self.X_train = df.values  # Feature values
        self.filename = splitext(split(f_name)[-1])[0]
        # print(self.filename)