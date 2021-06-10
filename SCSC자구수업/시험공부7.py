# Circle LinkedList
# setCurrent, moveRiht, moveLeft, append, insert, delete, print 

class Node:
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
    

class CL:
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.current = self.root
    
    def setCurrent(self, item):
        curNode = self.root
        if self.size == 0:
            return None
        else:
            a = 0
            while curNode.item != item:
                curNode = curNode.right
                a += 1
                if a > self.size:
                    print('목록에 존재하지 않는 item입니다.')
                    break
            self.current = curNode
            print('현재 위치는 \'%s\' 입니다.'%curNode.item)
            
    def moveRight(self):
        self.current = self.current.right
        print('현재 위치는 \'%s\' 입니다.'%self.current.item)
    
    def moveLeft(self):
        self.current = self.current.left
        print('현재 위치는 \'%s\' 입니다.'%self.current.item)
    
    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if self.size == 0:
            self.root = newNode
        else:
            for i in range(self.size-1):
                curNode = curNode.right
            curNode.right = newNode
            newNode.left = curNode
            newNode.right = self.root
            self.root.left = newNode
        self.size += 1
    
    def insert(self, index, item):
        curNode = self.root
        newNode = Node(item)
        if self.size == 0:
            self.root = newNode
        else:
            for i in range(index):
                preNode = curNode
                curNode = curNode.right
            preNode.right = newNode
            newNode.left = preNode
            newNode.right = curNode
            curNode.left = newNode
        self.size += 1
    
    def delete(self, item):
        curNode = self.root
        preNode = self.root
        if self.size == 0:
            return None
        else:
            a = 0
            if self.root.item == item:
                curNode = curNode.right
                for i in range(self.size-1):
                    preNode = preNode.right
                self.root = curNode
                self.root.left = preNode
                preNode.right = self.root
            else:
                while curNode.item != item:
                    preNode = curNode
                    curNode = curNode.right
                    a += 1
                    if a > self.size + 1:
                        print('목록 내에 존재하지 않는 item입니다.')
                        break
                preNode.right = curNode.right
                curNode.right.left = preNode
        self.size -= 1
        
    def print(self):
        curNode = self.root
        if self.size == 0:
            return None
        else:
            for i in range(self.size):
                print(curNode.item,end=" ")
                curNode = curNode.right
        print()
            
        
a = CL()
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
a.delete('사과')
a.print()
a.insert(2, '망고')
a.print()
a.delete('사과')
a.print()


a.setCurrent('배')

a.moveRight()
a.moveRight()
a.moveLeft()

