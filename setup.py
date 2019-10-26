# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:31:12 2019

@author: Mahdi Rahbar

This installation file was made by help of the following link: 
https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python
"""



from cx_Freeze import setup, Executable


base = "Win32GUI"    

executables = [Executable("main.py", base=base)]

packages = ["idna","PyQt5","numpy","joblib","sklearn","pandas","hazm","pickle",
            "re","string","collections","ntpath","docx","os"]# ,"PyQt5.QtGui","PyQt5.QtCore","PyQt5.QtWidgets"
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "app",
    options = options,
    version = "0.01",
    description = '<any description>',
    executables = executables
)