class Node:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if self.root == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
    
    def insert(self,idx , item):
        newNode = Node(item)
        curNode = self.root

        if idx == 0:
            newNode.link = self.root
            self.root = newNode
        elif idx > 0:
            for i in range(idx-1):
                curNode = curNode.link
            _tmp = curNode.link
            curNode.link = newNode
            newNode.link = _tmp
    
    def delete(self, item):
        curNode = self.root
        if curNode.item == item:
            self.root = self.root.link
        else:
            while curNode.link != None:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link

    def print(self):
        curNode = self.root
        while curNode != None:
            print(curNode.item, end=", ")
            curNode = curNode.link


fruits = LinkedList()
fruits.append('사과')
fruits.append('앵두')
fruits.append('포도')
fruits.insert(1,"귤")
fruits.print()
fruits.delete("사과")
fruits.print()


