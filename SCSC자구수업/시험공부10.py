# Tree

# 이진탐색트리!

class Node:
    def __init__(self, item = None):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        
    def inOrder(self):
        if self.item != None:
            if self.left:
                self.left.inOrder()
            print(self.item, end=" ")
            if self.right:
                self.right.inOrder()
    

class BST:
    def __init__(self):
        self.root = Node()
        self.size = 0
        
    def find(self, item): # 찾고자 하는 item이 존재하면, 그 item을, 아니면 그 부모노드를 return한다.
        if self.size == 0:
            return None
        else:
            preNode = None
            curNode = self.root
            while curNode != None:
                if curNode.item < item:
                    preNode = curNode
                    curNode = curNode.right
                elif curNode.item == item:
                    return curNode
                else:
                    preNode = curNode
                    curNode = curNode.left
            return preNode
    
    def getLchild(self, item):
        if self.size == 0:
            return None
        else:
            curNode = self.find(item)
            if curNode.item == item:
                if curNode.left != None:
                    curNode = curNode.left
                    print('\'%s\''%curNode.item)
                else:
                    print('지정하신 item의 Left값이 존재하지 않습니다.')
            else:
                print('목록 내에 item이 존재하지 않습니다.')
    
    def getRchild(self, item):
        if self.size == 0:
            return None
        else:
            curNode = self.find(item)
            if curNode.item == item:
                if curNode.right != None:
                    curNode = curNode.right
                    print('\'s\''%curNode.item)
                else:
                    print('지정하신 item의 right값이 존재하지 않습니다.')
            else:
                print('목록 내에 item이 존재하지 않습니다.')
                
    def getParent(self, item):
        if self.size == 0:
            return None
        else:
            curNode = self.find(item)
            if curNode.item != item:
                print('목록 내에 item이 존재하지 않습니다.')
            else:
                if curNode.item == self.root.item:
                    print('root node입니다.')
                else:
                    curNode = curNode.parent
                    print('\'%s\''%curNode.item)

    def insert(self, item):
        newNode = Node(item)
        curNode = self.find(item)
        if self.size == 0:
            self.root = newNode
        else:
            if curNode.item == item:
                print('목록 내에 item이 이미 존재합니다.')
            elif curNode.item < item:
                curNode.right = newNode
                newNode.parent = curNode
            else:
                curNode.left = newNode
                newNode.parent = curNode
        self.size += 1

    def delete(self, item):
        if self.size == 0:
            return None
        else:
            d = self.find(item)
            l = d.left
            r = d.right
            p = d.parent
            m = d.left
            if p != None:
                if l != None:
                    if p.item < d.item:
                        l.parent = p
                        p.right = l
                        while m.right != None:
                            m = m.right
                        if r != None:
                            m.right = r
                            r.parent = m
                    else:
                        l.parent = p
                        p.left = l
                        while m.right != None:
                            m = m.right
                        if r != None:
                            m.right = r
                            r.parent = m
                else:
                    if p.item < d.item:
                        if r != None:
                            p.right = r
                            r.parent = p
                    else:
                        if r != None:
                            p.left = r
                            r.parent = p
            else:
                if l != None:
                    while m.right != None:
                        m = m.right
                    if r != None:
                        m.right = r
                        r.parent = m
                    self.root = l
                else:
                    if r != None:
                        self.root = r
        self.size -= 1
        
    def print(self):
        if self.size == 0:
            return None
        else:
            self.root.inOrder()
        print()
        
        
        
b = BST()

b.insert(16)
b.insert(8)
b.insert(3)
b.insert(31)
b.insert(33)
b.insert(28)
b.insert(24)
b.insert(19)
b.insert(17)
b.insert(22)
b.insert(9)
b.insert(6)
b.insert(15)
b.insert(20)
b.insert(2)
b.insert(1)
b.insert(12)

b.print()

b.delete(3)

b.print()

b.delete(19)

b.print()

b.getLchild(12)
b.getRchild(12)
b.getParent(16)
