# double LinkedList

class DNode:
    def __init__(self, item = None, rlink = None, llink = None):
        self.rlink = rlink
        self.llink = llink
        self.item = item
        
class DLinkedList:
    def __init__(self):
        self.root = DNode()
        self.current = self.root
        
    def append(self, item):
        newNode = DNode(item)
        if self.root.item == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.rlink != None:
                curNode = curNode.rlink
            curNode.rlink = newNode
            curNode.llink = curNode
            
    def setCurrent(self, item):
        curNode = self.root
        if curNode.item == item:
            self.current = curNode
            print('현재 위치는',self.current.item,'입니다.')
        else:
            if curNode.item == item:
                self.current = curNode
                print('현재 위치는',self.current.item,'입니다.')
    
    def moveLeft(self):
        if self.current == self.root:
            print('맨 처음입니다.')
        else:
            self.current = self.current.llink
            print('현재 위치는 %s 입니다.' % self.current.item)
            
    def moveRight(self):
        if self.current.rlink == None:
            print('맨 마지막 입니다.')
        else:
            self.current = self.current.rlink
            print('현재 위치는 %s 입니다.' % self.current.item)

    def print(self):
        curNode = self.root
        print(curNode.item, end=' ')
        while curNode.rlink != None:
            curNode = curNode.rlink
            print(curNode.item,end=',')
        print()

    

a = DLinkedList()
print(a.root.item, a.root.rlink, a.root.llink)
a.append('사과')
a.append('배')
a.append('포도')
a.print()
a.setCurrent('배')

a.moveLeft()

