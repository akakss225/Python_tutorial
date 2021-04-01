# Cicle LinkedList

class CNode:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

class CircleLinkedList:
    def __init__(self):
        self.root = CNode()
        self.tail = CNode()
    
    def append(self, item):
        newNode = CNode(item)
        if self.root.item == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
        
    def current(self, item):
        newNode = CNode(item)
        curNode = self.root
        if curNode.item != newNode.item:
            if curNode.link == None and curNode.item != newNode.item:
                curNode = self.tail
            else:
                while curNode.item != newNode.item:
                    curNode = curNode.link
        print('현재 위치는 %s 입니다.' %curNode.item)
        
    def moveRight(self):
        curNode = self.root
        if curNode == None:
            print('리스트가 존재하지 않습니다.')
        else:
            if curNode.link == None:
                curNode.link = self.tail
                print('현재 위치는 %s 입니다.' %curNode.item)
            else:
                curNode = curNode.link
                print('현재 위치는 %s 입니다.' %curNode.item)
        
    
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
a.current('배')
a.moveRight()