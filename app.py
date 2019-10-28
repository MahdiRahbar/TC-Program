# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:28:50 2019

@author: Mahdi Rahbar
"""

from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QMessageBox, QGridLayout, QTableWidgetItem,
                             QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
from tc import ImportData, Preprocessor, classifier
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSlot
from GUI import gui
import sys
from os.path import expanduser

class TCApp(gui.Ui_MainWindow, QMainWindow):
    """ The main class to connect
    different parts of module: tc 
    to GUI.
    
    functions
    -------------------
    Init_GUI
    get_data_path
    Classifier_trggr
    Display_Table
    Progress_Bar_hndle
    Display_Status
    set_pbar_range
    """
    def __init__(self):
        super(TCApp ,self).__init__()

        self.setupUi(self)

        self.user_in = None  # Stores user's data and input
        self.data_info = None
        self.init_GUI()

        self.Classification_Start_Button.setEnabled(False)

        self.prog = 0
        self.Classification_Progress_Bar.setRange(0, 100)
        self.Classification_Progress_Bar.setValue(self.prog)
        self.status ='status'
        self.imported_data_number=0
    def init_GUI(self):
        """
        Initialize the GUI of application
        """

        # Threads
        self.__threads = []

        # Buttons
        self.Path_Open_Button.clicked.connect(self.get_data_path)
        self.Classification_Start_Button.clicked.connect(self.Classifier_trggr)
        self.Classification_Start_Button.clicked.connect(self.Progress_Bar_hndle)



    def get_data_path(self):
        """
        Gets the dataset path from a user.
        """

        data_filename = QFileDialog.getExistingDirectory(self, "Open a folder",
                                                            "",
                                                            QFileDialog.ShowDirsOnly)
        if data_filename:

            self.Address_Bar.setText(str(data_filename))
            self.Classification_Start_Button.setEnabled(True)

            # Enable widgets in Read group box
            for w in self.Classification_Start_Button.children():

                if not isinstance(w, QGridLayout):

                    w.setEnabled(True)               

    def Classifier_trggr(self):
        """
        Loads a dataset.
        """

        self.data_reader = ImportData.Data_Reader(self.Address_Bar.text(), self.Address_Bar.text() , True) # , True if self.header_check.isChecked() else False
                                      
        self.data_reader.Text_Maker_Save()

        self.user_in , self.doc_names= self.data_reader.Corpus_Reader()
        self.prog =0 
        self.Progress_Bar_hndle()

        self.set_pbar_range(100)
        
        self.Stop_Word_List = ''
        self.PreProc = Preprocessor.PreProcessing(self.user_in, self.Stop_Word_List)
        self.prog=10
        self.Progress_Bar_hndle()

        self.status ='Pre-processing...'
        self.Display_Status()
        self.PreProc.String_Splitter()
        self.prog =30 
        self.Progress_Bar_hndle()

        self.status ='Pre-processing...'
        self.Display_Status()
        self.PreProc.TextCleaner()
        self.prog=70
        self.Progress_Bar_hndle()

        self.status ='Pre-processing...'
        self.Display_Status()
        self.PreProc.wordToString()
        self.prog=80
        self.Progress_Bar_hndle()

        self.status ='Classification...'
        self.Display_Status()
        self.Preprocessed_Data = self.PreProc.Data_Vectorizer()
        self.prog = 90
        self.Progress_Bar_hndle()

        self.clf = classifier.InputClassifier(self.Preprocessed_Data)
        self.status ='Done!'
        self.Display_Status()
        self.prog = 100
        self.Progress_Bar_hndle()

        self.clf.SVCClassifier()

        self.Display_Table()
    def Display_Table(self):
        self.label_list = self.clf.Show_Label()
        self.no_samples = len(self.label_list)
        self.Proba_Matrix = self.clf.SVC_Proba()
        self.result_text = ''
        no_counter = 0
        _, col = self.Proba_Matrix.shape
        self.Result_Table.setRowCount(self.no_samples)
        for label in self.label_list:
            no_counter += 1
            self.Result_Table.setItem(no_counter-1, 0, QTableWidgetItem(str(no_counter)))

            if label== "fa":
                self.result_text = "فنی" 
            if label== "pa":
                self.result_text =  "پایه" 
            if label== "pe":
                self.result_text = "پزشکی" 
            if label== "ho":
                self.result_text = "هنر"
            if label== "en":
                self.result_text =  "انسانی" 
            self.Result_Table.setItem(no_counter-1, 1, QTableWidgetItem( self.result_text))
            self.Result_Table.setItem(no_counter-1, 0, QTableWidgetItem(self.doc_names[no_counter-1]))

            for i in range(col):
                self.Result_Table.setItem(no_counter-1, i+2, QTableWidgetItem("%.2f"%self.Proba_Matrix[no_counter-1,i]))


    def Progress_Bar_hndle(self):
        
        self.Classification_Progress_Bar.setValue(self.prog)

        

    def Display_Status(self):
        self.Process_Status_Label.setText(self.status)


    @pyqtSlot(int)
    def set_pbar_range(self, pbar_rng):
        """
        Sets range of the progress bar by the grid search thread.

        Parameters
        ----------
        pbar_rng : int
            range of the progress bar.
        """

        self.Classification_Progress_Bar.setRange(0, pbar_rng)

    @pyqtSlot(int, str, str, str)
    def update_gs_info(self, pbar_val): #  ,curr_acc, best_acc, elapsed_t
        """
        Updates current value of the progress bar, current accuracy, and best
        accuract, elapsed time.

        Parameters
        ----------
        pbar_val : int
            value of progress bar.

        curr_acc
        """

        self.Classification_Progress_Bar.setValue(pbar_val)



def main():

    app = QApplication(sys.argv)
    tcapp = TCApp()
    tcapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()