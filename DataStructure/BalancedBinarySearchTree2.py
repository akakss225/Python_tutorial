# AVL Tree
# 모든 노드에 대하여 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차가 1 이하인 이진탐색트리
# 즉, 각 노드의 높이를 강제하여 만든다. h = O(log n)으로 만들어줌.

class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    def inOrder(self):
        if self.key != None:
            if self.left:
                self.left.inOrder()
            print(self.key, end=" ")
            if self.right:
                self.right.inOrder()
    
    def preOrder(self):
        if self.key != None:
            print(self.key, end=" ")
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
                
    def postOrder(self):
        if self.key != None:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(self.key, end=" ")

class BST:
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    def find(self, key):
        if self.size == 0:
            return None
        else:
            preNode = None
            curNode = self.root
            if curNode.key == key:
                return curNode
            else:
                while curNode != None:
                    if curNode.key == key:
                        return curNode
                    elif curNode.key < key:
                        preNode = curNode
                        curNode = curNode.right
                    else:
                        preNode = curNode
                        curNode = curNode.left
                return preNode
                    
    def insert(self, key):
        preNode = self.find(key)
        newNode = Node(key)
        if self.size == 0:
            self.root = newNode
        else:
            if key == preNode.key:
                print('Tree already has a key')
            else:
                if key < preNode.key:
                    preNode.left = newNode
                    newNode.parent = preNode
                else:
                    preNode.right = newNode
        self.size += 1
                    
    def delete(self, key):
        if self.size == 0:
            return None
        else:
            d = self.find(key)
            l = d.left
            r = d.right
            p = d.parent
            max = d.left
            if d.key != key:
                return None
            else:
                if p != None:
                    if l != None:
                        if p.key < key:
                            l.parent = p
                            p.right = l
                            while max.right != None:
                                max = max.right
                            if r != None:
                                max.right = r
                                r.parent = max
                            else:
                                return
                        else:
                            l.parent = p
                            p.left = l
                            while max.right != None:
                                max = max.right
                            if r != None:
                                max.right = r
                                r.parent = max
                            else:
                                return
                    else:
                        if p.key < key:
                            if r != None:
                                p.right = r
                                r.parent= p
                            else:
                                p.right = None
                        else:
                            if r != None:
                                p.left = r
                                r.parent = p
                            else:
                                p.left = None
                else:
                    if l != None:
                        self.root = l
                        while max.right != None:
                            max = max.right
                        if r != None:
                            max.right = r
                            r.parent = max
                        else:
                            return
                    else:
                        if r != None:
                            self.root = r
                        else:
                            return None
        self.size -= 1
                      
                    
    def printpre(self):
        self.root.preOrder()
        print()
        
    def printin(self):
        self.root.inOrder()
        print()
        
    def printpost(self):
        self.root.postOrder()
        print()
        
t = BST()
t.insert(10)
t.insert(2)
t.insert(1)
t.insert(11)
t.insert(5)
t.insert(9)
t.insert(3)
t.insert(17)

t.printpre()
t.printin()
t.printpost()

t.delete(3)
t.printpre()
t.printin()
t.printpost()