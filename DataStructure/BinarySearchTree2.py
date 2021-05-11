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
                            d = l
                            d.parent = p
                            p.left = d
                            while m != None:
                                m = m.right
                            if r != None:
                                m.right = r
                                r.parent = m
                        else:
                            d = l
                            d.parent = p
                            p.right = d
                            while m != None:
                                m = m.right
                            if r != None:
                                m.right = r
                                r.parent = m
                    else:
                        if key < p.key:
                            d = r
                            d.parent = p
                            p.left = d
                        else:
                            d = r
                            d.parent = p
                            p.right = d
                else:
                    if l != None:
                        d = l
                        d.parent = None
                        while m != None:
                            m = m.right
                        if r != None:
                            m.right = r
                            r.parent = m
                    else:
                        d = r
                        d.parent = None
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

b.delete(2)
b.print()
print(b.size)