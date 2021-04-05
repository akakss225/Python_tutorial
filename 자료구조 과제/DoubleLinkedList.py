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
            return 0
        else:
            while curNode.rlink != None:
                curNode = curNode.rlink
                result += 1
            return result
            
    def find(self, item):
        curNode = self.root
        index = 1
        if curNode.item == item:
            return index
        else:
            while curNode.rlink != None:
                curNode = curNode.rlink
                index += 1
                if curNode.item == item:
                    return index
            return -1
        
    def nodeFind(self, index):
        curNode = self.root
        if index < 0 or self.size() == 0:
            return None
        
        if index == 0:
            return curNode.item
        elif index >= self.size():
            return None
        else:
            for i in range(index):
                curNode = curNode.rlink
            return curNode.item
    
    def insert(self, item, idx):
        curNode = self.root
        newNode = DNode(item)
        if idx < 0 or idx > self.size():
            return None
        elif idx == 0:
            temp = self.root
            self.root = newNode
            newNode.rlink = temp
        else:
            for i in range(1,idx):
                curNode = curNode.rlink
            temp = curNode.rlink
            curNode.rlink = newNode
            newNode.rlink = temp
            newNode.llink = temp.llink
            
    def delete(self, item):
        curNode = self.root
        if self.root.item == item:
            self.root = self.root.rlink
            self.root.llink = None
        else:
            while curNode.rlink != None:
                curNode = curNode.rlink
                if curNode.rlink == None:
                    if curNode.item == item:
                        curNode.llink.rlink = curNode.rlink
                else:
                    if curNode.item == item:
                        curNode.llink.rlink = curNode.rlink
                        curNode.rlink.llink = curNode.llink
                        
            
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
print(a.size())
print(a.find('사과'))
print(a.find('배'))
print(a.find('귤'))
print(a.find('포도'))
print(a.find('딸기'))
print(a.nodeFind(3))
a.insert('체리',3)
a.print()
a.delete('배')
a.print()