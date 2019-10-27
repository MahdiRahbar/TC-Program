# # -*- coding: utf-8 -*-
# """
# Created on Sat Oct 26 13:31:12 2019

# @author: Mahdi Rahbar

# This installation file was made by help of the following link: 
# https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python
# """


# import sys
# from cx_Freeze import setup, Executable


# base = "Win32GUI"    

# executables = [Executable("main.py", base=base)]
# # includefiles = ['./app.py','./tc', './tc/classifier.py', './tc/ImportData.py',
# #                 './tc/Preprocessor.py' , './tc/model/SVCmodel_Proba.sav',
# #                 './tc/model/label_encoder.joblib','./tc/model/count_vect.pkl'
# #                 ,'./GUI/gui.py']

packages = ["idna","numpy","joblib","sklearn","pandas","hazm","pickle",
            "re","string","collections","ntpath","docx","os","nltk"]# ,"PyQt5.QtGui","PyQt5.QtCore","PyQt5.QtWidgets"
# options = {
#     'build_exe': {    
#         'packages':packages #,'include_files':includefiles
#     },    
# }

# setup(
#     name = "TCApp",
#     options = options,
#     version = "0.01",
#     description = 'The first release of the TC-App.',
#     executables = executables
# )


# # includefiles = ['README.txt', 'CHANGELOG.txt', 'helpers\uncompress\unRAR.exe', , 'helpers\uncompress\unzip.exe']
# # includes = []
# # excludes = ['Tkinter']


# # setup(
# #     name = 'myapp',
# #     version = '0.1',
# #     description = 'A general enhancement utility',
# #     author = 'lenin',
# #     author_email = 'le...@null.com',
# #     options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
# #     executables = [Executable('janitor.py')]
# # )



setup(
name="TCApp",
version="0.0.1",
description="Thesis Classifier",
# long_description=README,
# long_description_content_type="text/markdown",
# url="https://github.com/MahdiRahbar/TC-program" ,
author="Mahdi Rahbar",
# author_email="office@realpython.com",
# license="MIT",
# classifiers=[
#     "License :: OSI Approved :: MIT License",
#     "Programming Language :: Python",
#     # "Programming Language :: Python :: 2",
#     "Programming Language :: Python :: 3",
# ],
# packages=["tc","GUI"],
include_package_data=True,
install_requires=packages,
entry_points={"gui_scripts": ["TCApp=app:main"]},
)