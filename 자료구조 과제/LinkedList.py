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

    def insert(self, idx, item):
        newNode = Node(item)
        curNode = self.root
        if idx == 0:
            _tmp = self.root
            self.root = newNode
            newNode.link = _tmp
        else:
            for i in range(idx-1):
                curNode = curNode.link
            _tmp = curNode.link
            curNode.link = newNode
            newNode.link = _tmp

    def delete(self, item):
        preNode = curNode = self.root
        if curNode.item == item:
            self.root = curNode.link
        else:
            while curNode.link != None:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link

    def size(self):
        listSize = 1
        curNode = self.root
        while curNode.link != None:
            curNode = curNode.link
            listSize += 1
        return listSize

    def find(self, item):
        curNode = self.root
        curIdx = 0
        if curNode.item == item:
            return 0
        else:
            while curNode.link != None:
                curNode = curNode.link
                curIdx += 1
                if curNode.item == item:
                    return curIdx
        return -1

    def nodeFind(self, idx):
        if idx <0 or idx >= self.size():
            return None
        curNode = self.root
        if idx == 0:
            return self.root
        else:
            for i in range(idx):
                curNode = curNode.link
            return curNode

    def print(self):
        curNode = self.root
        print(curNode.item, end = ', ')
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item, end = ', ')
        print()

fruits = LinkedList()
fruits.append("사과")
fruits.append("오렌지")
fruits.append("포도")
fruits.append("복숭아")

fruits.delete("복숭아")
fruits.print()