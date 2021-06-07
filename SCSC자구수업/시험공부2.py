# LinkedList

class Node:
    def __init__(self, item = None):
        self.item = item
        self.link = None

class LinkedList:
    def __init__(self):
        self.l = []
        self.root = Node()

    def append(self, item):
        curNode = self.root
        newNode = Node(item)
        if self.root.item == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
        
    def insert(self, index, item):
        newNode = Node(item)
        curNode = self.root
        
        if index == 0:
            self.root = newNode
            newNode.link = curNode
        else:
            for i in range(index):
                preNode = curNode
                curNode = curNode.link
            preNode.link = newNode
            newNode.link = curNode
            
    def delete(self, item):
        preNode = self.root
        curNode = self.root
        if self.root.item == None:
            return None
        else:
            if self.root.item == item:
                self.root = curNode.link
            else:
                while curNode.item != item:
                    preNode = curNode
                    curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                else:
                    return None
            
    

    def print(self):
        curNode = self.root
        if self.root != None:
            while curNode != None:
                print(curNode.item, end=" ")
                curNode = curNode.link
        print()

l = LinkedList()

l.append('사과')
l.append('귤')
l.append('배')
l.append('포도')

l.print()

l.delete('사과')

l.print()

l.delete('포도')

l.print()

l.insert(1, '망고')

l.print()

l.insert(3, '수박')

l.print()

l.insert(0, '블루베리')

l.print()