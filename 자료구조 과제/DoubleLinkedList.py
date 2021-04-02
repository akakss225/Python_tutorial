# Double LinkedList

class DNode:
    def __init__(self, item = None, llink = None, rlink = None):
        self.item = item
        self.llink = llink
        self.rlink = rlink
        
class DoubleLinkedList:
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
            newNode.llink = curNode
            curNode.rlink = newNode
    
    def setCurrent(self, item):
        curNode = self.root
        if self.current.item == item:
            print('현재 위치는 %s 입니다.'%self.current.item)
        else:
            while curNode.item != item:
                curNode = curNode.rlink
            self.current = curNode
            print('현재 위치는 %s 입니다.'%self.current.item)
    
    def moveLeft(self):
        if self.current.llink == None:
            print('리스트의 가장 왼쪽입니다.')
        else:
            self.current = self.current.llink
            print('현재 위치는 %s입니다.'%self.current.item)

    def moveRight(self):
        if self.current.rlink == None:
            print('리스트의 가장 오른쪽입니다.')
        else:
            self.current = self.current.rlink
            print('현재 위치는 %s입니다.'%self.current.item )
            
    def size(self):
        result = 1
        curNode = self.root
        if curNode.item == None:
            print(0)
        else:
            while curNode.rlink != None:
                curNode = curNode.rlink
                result += 1
            print(result)
            
    def find(self, item):
        curNode = self.root
        index = 1
        if curNode.item == item:
            return index
        else:
            while curNode.item != item:
                curNode = curNode.rlink
                index += 1
                if curNode.item == item:
                    return index

    def print(self):
        curNode = self.root
        if curNode.item == None:
            print('there is no list')
        else:
            print(curNode.item,end=',')
            while curNode.rlink != None:
                curNode = curNode.rlink
                print(curNode.item,end=',')
        print()

a = DoubleLinkedList()
a.append('사과')
a.append('배')
a.append('귤')
a.append('포도')
a.print()
a.setCurrent('배')
a.moveLeft()
a.moveRight()
a.size()
print(a.find('사과'))
print(a.find('배'))
print(a.find('귤'))
print(a.find('포도'))
print(a.find('딸기'))
