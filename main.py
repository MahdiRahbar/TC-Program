# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:47:48 2019

@author: Mahdi Rahbar
"""
from tc import ImportData, Preprocessor, classifier

if __name__ == "__main__":
    Path = './test/'
    save_path = Path
    keep_text = True
    doc2txt = ImportData.DocToText(Path,save_path, keep_text)
    doc2txt.Text_Maker_Save()
    
    D = ImportData.DataImport(Path)
    Data = D.Corpus_Reader()

    Stop_Word_List = ''
    PreProc = Preprocessor.PreProcessing(Data, Stop_Word_List)
    PreProc.String_Splitter()
    PreProc.TextCleaner()
    PreProc.wordToString()
    Data = PreProc.Data_Vectorizer()
    # print(Data.shape)
    clf = classifier.InputClassifier(Data)
    print(clf.SVCClassifier())
    print(clf.Show_Label())
