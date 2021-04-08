import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\akaks\\Documents\\Python_tutorial\\PyQT\\num1.ui")[0]

class WindowClass(QMainWidow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
app = QApplcation(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()