import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, qApp, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *

form_class = loadUiType("imageViewer.ui")[0]

class Node:
    def __init__(self, item = None):
        self.item = item
        self.link = None

class CirclelinkedList:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.current = self.root
    
    def append(self, item):
        newNode = Node(item)
        if self.root.item == None:
            self.root = newNode
        else:
            temp = self.tail.link
            self.tail.link = newNode
            newNode.link = temp
            self.tail = newNode
        
    def listSize(self):
        curNode = self.root
        num = 1
        while curNode.link != self.root:
            curNode = curNode.link
            num += 1
        return num
    
    def setCurrent(self, item):
        curNode = self.root
        if curNode.item == item:
            self.current = curNode
        else:
            while curNode.item != item:
                curNode = curNode.link
            self.current = curNode
    
    def moverNext(self):
        self.current = self.current.link
        print('현재 위치는', self.current,'입니다.')
    
    def insert(self, item):
        newNode = Node(item)
        temp = self.current.link
        self.current = newNode
        newNode.link = temp
        if self.current == self.tail:
            self.tail = newNode
    
    def delete(self, item):
        check = False
        curNode = self.root
        if curNode.item == item:
            self.root = self.root.link
            self.tail.link = self.root
            check = True
        else:
            while curNode.item != self.root:
                preNode = curNode
                curNode = curNode.link
                if curNode.item ==item:
                    preNode.link = curNode.link
                    if curNode == self.tail:
                        self.tail = preNode
                    check = True
        if check == False:
            print('Can\'t delete')
        
    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != self.root:
            curNode = curNode.link
            print(curNode.item)
        

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.actionSelect.triggered.connect(self.fileSelect)
        self.pushButton.clicked.connect(self.moveNextClick)
        self.slideShowButton.clicked.connect(self.slideShowClick)
        self.actionExit.triggered.connect(qApp.quit)

    def fileSelect(self):
        dirName = QFileDialog.getExistingDirectory(self, 'Open Folder', 'E:/MyPhoto/Test')
        self.files = CirclelinkedList()
        for file in glob.glob(os.path.join(dirName,'*.jpg')):
            self.files.append(file)
        self.files.current = self.files.root
        self.qPixmapVar.load(self.files.current.item)
        self.qPixmapVar = self.qPixmapVar.scaled(700, 400, aspectRatioMode = True)
        self.label.setPixmap(self.qPixmapVar)
    
    def moveNextClick(self):
        self.files.moverNext()
        self.qPixmapVar.load(self.files.current.item)
        self.qPixmapVar = self.qPixmapVar.scaled(700, 400, aspectRatioMode = True)
        self.label.setPixmap(self.qPixmapVar)
    
    def slideShowClick(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.moveNextClick)
        self.timer.start(3000)
        
app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec_()