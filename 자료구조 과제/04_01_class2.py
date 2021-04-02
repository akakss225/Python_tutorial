# Cicle LinkedList

class CNode:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

class CircleLinkedList:
    def __init__(self):
        self.root = CNode()
        self.tail = CNode()
        self.current = self.root
    
    def append(self, item):
        newNode = CNode(item)
        if self.root.item == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
        self.tail = newNode
        
        
    def setCurrent(self, item):
        curNode = self.root
        if curNode.item == item:
            self.current = curNode
        else:
            while curNode.item != item:
                curNode = curNode.link
            self.current = curNode
        print('현재 위치는 %s 입니다.' %self.current.item)
        
    def moveRight(self):
        if self.current == self.tail:
            self.current = self.root
            print('현재 위치는 %s 입니다.' %self.current.item)
        else:
            self.current = self.current.link
            print('현재 위치는 %s 입니다.' %self.current.item)
        

    def print(self):
        curNode = self.root
        print(curNode.item,end=',')
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item,end=',')
        print()


a = CircleLinkedList()
a.append('사과')
a.append('포도')
a.append('배')
a.append('귤')
a.print()
a.setCurrent('귤')
a.moveRight()