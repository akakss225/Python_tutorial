# Circle LinkedList

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
        if self.size == 0:
            return None
        else:
            temp = self.root
            if self.root.item == item:
                curNode = curNode.right
                for i in range(self.size):
                    temp = temp.right
                curNode.left = temp
                self.root = curNode
                
            a = 0
            while curNode.item != item:
                preNode = curNode
                curNode = curNode.right
                a += 1
                if a > self.size:
                    print('\'%s\'는 리스트에 존재하지 않습니다.'%item)
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
a.delete('망고')
a.print()
# a.insert(2, '망고')
# a.print()
# a.delete('사과')
# a.print()