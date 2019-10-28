# # -*- coding: utf-8 -*-
# """
# Created on Sat Oct 26 13:31:12 2019

# @author: Mahdi Rahbar

# This installation file was made by help of the following link: 
# https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python
# """


import sys
from cx_Freeze import setup, Executable


base = "Win32GUI"    

executables = [Executable("main.py", base=base)]
# includefiles =['./tc/model/count_vect.pkl','./tc/model/SVCmodel_Proba.sav','./tc/model/label_encoder.joblib']

packages = ["tc","GUI","idna","numpy","joblib","sklearn","pandas","hazm","pickle",
            "re","string","collections","ntpath","docx","os","nltk"]
options = {
    'build_exe': {    
        'includes': ['atexit'],'packages':packages ,  # ,'app','tc/classifier','tc/ImportData','tc/Preprocessor','GUI/gui.py'
        # 'include_files':includefiles
    },    
}

setup(
    name = "TCApp",
    options = options,
    version = "0.01",
    description = 'The first release of the TC-App.',
    executables = executables
)