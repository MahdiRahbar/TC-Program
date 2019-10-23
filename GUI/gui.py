# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 444)
        MainWindow.setMinimumSize(QtCore.QSize(640, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 621, 81))
        self.groupBox.setObjectName("groupBox")
        self.Path_Open_Button = QtWidgets.QPushButton(self.groupBox)
        self.Path_Open_Button.setGeometry(QtCore.QRect(550, 20, 61, 21))
        self.Path_Open_Button.setObjectName("Path_Open_Button")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setObjectName("label")
        self.Address_Bar = QtWidgets.QLineEdit(self.groupBox)
        self.Address_Bar.setGeometry(QtCore.QRect(40, 20, 501, 20))
        self.Address_Bar.setObjectName("Address_Bar")
        self.Text_Saving_Check_Box = QtWidgets.QCheckBox(self.groupBox)
        self.Text_Saving_Check_Box.setGeometry(QtCore.QRect(40, 50, 121, 17))
        self.Text_Saving_Check_Box.setObjectName("Text_Saving_Check_Box")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 621, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 601, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.Classification_Start_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Classification_Start_Button.setObjectName("Classification_Start_Button")
        self.horizontalLayout_2.addWidget(self.Classification_Start_Button)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.Classification_Progress_Bar = QtWidgets.QProgressBar(self.groupBox_2)
        self.Classification_Progress_Bar.setGeometry(QtCore.QRect(20, 60, 581, 23))
        self.Classification_Progress_Bar.setProperty("value", 24)
        self.Classification_Progress_Bar.setObjectName("Classification_Progress_Bar")
        self.Process_Status_Label = QtWidgets.QLabel(self.groupBox_2)
        self.Process_Status_Label.setGeometry(QtCore.QRect(220, 90, 181, 21))
        self.Process_Status_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Process_Status_Label.setObjectName("Process_Status_Label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 621, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Output_Text = QtWidgets.QTextBrowser(self.groupBox_3)
        self.Output_Text.setGeometry(QtCore.QRect(15, 20, 591, 111))
        self.Output_Text.setObjectName("Output_Text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Import"))
        self.Path_Open_Button.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "Path:"))
        self.Text_Saving_Check_Box.setText(_translate("MainWindow", "Save the Plant Text"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Classification"))
        self.Classification_Start_Button.setText(_translate("MainWindow", "Start"))
        self.Process_Status_Label.setText(_translate("MainWindow", "Status "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

