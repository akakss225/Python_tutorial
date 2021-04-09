# Open and Save function

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\akaks\Documents\\Python_tutorial\\PyQT\\num4.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        with open(fname[0]) as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)
        print('open {}!!'.format(fname[0]))
        
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        data = self.plainTextEdit.toPlainText()
        with open(fname[0], 'w') as f:
            f.write(data)
        
        print('save {}!!'.format(fname[0]))
        

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()