# Double LikedList
# append, insert, delet, current, moveleft, moveright, print 구현


class Node:
    def __init__(self, item = None):
        self.item = item
        self.llink = None
        self.rlink = None
        

class DL:
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.current = self.root

    def append(self, item):
        curNode = self.root
        newNode = Node(item)
        if self.size == 0:
            self.root = newNode
        else:
            while curNode.rlink != None:
                curNode = curNode.rlink
            curNode.rlink = newNode
            newNode.llink = curNode
        self.size += 1
    
    def insert(self, index, item):
        curNode = self.root
        newNode = Node(item)
        if index == 0:
            self.root = newNode
            newNode.rllink = curNode
            curNode.llink = self.root
        else:
            for i in range(index):
                preNode = curNode
                curNode = curNode.rlink
            preNode.rlink = newNode
            newNode.llink = preNode
            newNode.rlink = curNode
            curNode.llink = newNode
        self.size += 1
    
    def delete(self, item):
        curNode = self.root
        if self.size == 0:
            return None
        else:
            if self.root.item == item:
                curNode = curNode.rlink
                curNode.llink = None
                self.root = curNode
            else:
                while curNode.item != item:
                    preNode = curNode
                    curNode = curNode.rlink
                preNode.rlink = curNode.rlink
                curNode.rlink.llink = preNode
        self.size -= 1
    
    def currentLocation(self, item):
        curNode = self.root
        if self.root.item == item:
            self.current == curNode
            print('현재위치는 %s 입니다.'%self.current.item)
        else:
            while curNode.item != item:
                curNode = curNode.rlink
            self.current = curNode
            print('현재위치는 %s 입니다.'%self.current.item)
    
    def moveLeft(self):
        if self.current.llink == None:
            print('맨 앞입니다.')
        else:
            self.current = self.current.llink
            print('현재 위치는 %s 입니다.'%self.current.item)
    
    def moveRight(self):
        if self.current.rlink == None:
            print('맨 마지막 입니다.')
        else:
            self.current = self.current.rlink
            print('현재 위치는 %s 입니다.'%self.current.item)

    def print(self):
        curNode = self.root
        if self.size == 0:
            return None
        else:
            while curNode.rlink != None:
                print(curNode.item, end=" ")
                curNode = curNode.rlink
            print(curNode.item)
        
a = DL()
a.append('사과')
a.append('배')
a.append('포도')
a.append('딸기')
a.append('블루베리')
a.append('귤')
a.append('체리')
a.append('망고')
a.append('수박')
a.print()
a.delete('망고')
a.print()
a.insert(2, '망고')
a.print()
a.delete('사과')
a.print()

a.currentLocation('망고')

a.moveLeft()
a.moveLeft()

a.moveRight()
a.moveRight()

a.currentLocation('수박')
a.moveRight()