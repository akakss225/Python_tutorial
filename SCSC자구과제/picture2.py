import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\akaks\\Documents\\Python_tutorial\\자료구조 과제\\picture.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
