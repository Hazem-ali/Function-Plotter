# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mplwidget import MplWidget
import error
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 550))
        MainWindow.setMaximumSize(QSize(700, 550))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.FunctionData = QLineEdit(self.centralwidget)
        self.FunctionData.setObjectName(u"FunctionData")
        self.FunctionData.setGeometry(QRect(90, 120, 251, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 20, 301, 61))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.FunctionLabel = QLabel(self.centralwidget)
        self.FunctionLabel.setObjectName(u"FunctionLabel")
        self.FunctionLabel.setGeometry(QRect(90, 100, 121, 16))
        self.Minx = QLabel(self.centralwidget)
        self.Minx.setObjectName(u"Minx")
        self.Minx.setGeometry(QRect(360, 100, 41, 16))
        self.MinX_Value = QLineEdit(self.centralwidget)
        self.MinX_Value.setObjectName(u"MinX_Value")
        self.MinX_Value.setGeometry(QRect(360, 120, 61, 21))
        self.Maxx = QLabel(self.centralwidget)
        self.Maxx.setObjectName(u"Maxx")
        self.Maxx.setGeometry(QRect(440, 100, 51, 16))
        self.MaxX_Value = QLineEdit(self.centralwidget)
        self.MaxX_Value.setObjectName(u"MaxX_Value")
        self.MaxX_Value.setGeometry(QRect(440, 120, 61, 21))
        self.PlotButton = QPushButton(self.centralwidget,clicked = lambda:self.Plot_Graph())
        self.PlotButton.setObjectName(u"pushButton")
        self.PlotButton.setGeometry(QRect(520, 120, 101, 23))
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setGeometry(QRect(140, 170, 411, 311))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.showMessage("Welcome to Function Plotter",10*1000)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def Plot_Graph(self):
        # Empty Check
        if self.FunctionData.text() == '':
            self.Open_Error_Window("Cannot plot empty function")
            self.statusBar.showMessage("Plot Failed",10*1000)
            print(self.statusBar.currentMessage())
            
            return
        
        min_x = 0
        max_x = 0
        try:
            min_x = int(self.MinX_Value.text())
            max_x = int(self.MaxX_Value.text())
        except:
            self.Open_Error_Window("Please Write Valid x Limits..!")
            self.statusBar.showMessage("Plot Failed",10*1000)
            return
        
        # Preparing expression for evaluation
        expression = self.Prepare_Expression(self.FunctionData.text())
        x = np.linspace(min_x,max_x,100)
        y = 0
        try:
            y = eval(expression)
        except:
            self.Open_Error_Window("Please Write Valid Function..!")
            self.statusBar.showMessage("Plot Failed",10*1000)
            return
        
        # Drawing results        
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.plot(x, y)
        self.MplWidget.canvas.draw()
        self.statusBar.showMessage("Plot Success",10*1000)
    
    def Open_Error_Window(self, message):
        self.window = QDialog()
        self.ui = error.Ui_Dialog(message)
        self.ui.setupUi(self.window)
        self.window.show()
        
    def Prepare_Expression(self, expression):
        # prepare expression to enter eval() function
        result = ''
        for i in expression:
            if i == '^':
                result += '**'
            else:
                result += i
        return result
            
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.FunctionLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Function Here", None))
        self.Minx.setText(QCoreApplication.translate("MainWindow", u"Min x", None))
        self.Maxx.setText(QCoreApplication.translate("MainWindow", u"Max x", None))
        self.PlotButton.setText(QCoreApplication.translate("MainWindow", u"Plot Function", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())