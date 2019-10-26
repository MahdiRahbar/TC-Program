# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:31:12 2019

@author: Mahdi Rahbar
"""



from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna","tc","GUI"]
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