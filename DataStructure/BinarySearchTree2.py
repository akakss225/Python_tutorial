class BNode:
    def __init__(self, key = None):
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
    

class BST:
    def __init__(self):
        self.root = BNode()
        self.size = 0
    
    def find(self, key):
        if self.size == 0:
            return None
        else:
            curNode = self.root
            preNode = None
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
        tmp = self.find(key)
        newNode = BNode(key)
        if self.size == 0:
            self.root = newNode
        else:
            newNode.parent = tmp
            if tmp.key == key:
                print('key값이 이미 존재합니다.')
            else:
                if tmp.key < key:
                    tmp.right = newNode
                else:
                    tmp.left = newNode
        self.size += 1
    
    # DeleteByMerging의 경우, 삭제하는 값의 왼쪽노드를 삭제될 곳으로 가져오고, 가져온 서브트리의 가장 큰값에 기존의 오른쪽 노드르 붙히는것
    def delete(self, key):
        if self.size == 0:
            return None
        else:
            d = self.find(key)
            l = d.left
            r = d.right
            p = d.parent
            m = d.left
            
            if d.key != key:
                print('key값이 존재하지 않습니다.')
            else:
                if p != None:
                    if l != None:
                        if key < p.key:
                            l.parent = p
                            p.left = l
                            while m.right != None:
                                m = m.right 
                            if r != None:
                                m.right = r
                                r.parent = m
                        else:
                            l.parent = p
                            p.right = l
                            while m.right != None:
                                m = m.right
                            if r != None:
                                m.right = r
                                r.parent = m
                    else:
                        if r != None:
                            if key < p.key:
                                r.parent = p
                                p.left = r
                            else:
                                r.parent = p
                                p.right = r
                        else:
                            d = None
                            if key < p.key:
                                p.left = None
                            else:
                                p.right = None
                else:
                    if l != None:
                        self.root = l
                        while m.right != None:
                            m = m.right
                        if r != None:
                            m.right = r
                            r.parent = m
                    else:
                        if r != None:
                            self.root = r
                        else:
                            self.root = None
        self.size -= 1
        
    def print(self):
        print(self.root.inOrder())

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
print(b.size)

b.delete(1)
b.print()
print(b.size)