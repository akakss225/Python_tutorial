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
    
    # DeleteByCopying의 경우, 삭제하고자 하는 노드의 왼쪽 서브트리의 가장 큰 값을 삭제하고자 하는 노드에 넣어주고, 카피가 된 값은 없애준다.
    def delete(self, key):
        if self.size == 0:
            return None
        else:
            d = self.find(key)
            r = d.right
            l = d.left
            p = d.parent
            max = d.left
            
            if d.key != key:
                print('key값이 존재하지 않습니다.')
            else:
                if p != None:
                    if l != None:
                        while max.right != None:
                            max = max.right
                        pre = max.parent
                        templ = max.left
                        d.key = max.key
                        if max == l:
                            if templ != None:
                                d.left = templ
                                templ.parent = d
                            else:
                                d.left = None
                        else:
                            if templ != None:
                                pre.right = templ
                                templ.parent = pre
                            else:
                                pre.right = None
                                max.parent = None
                    else:
                        if r != None:
                            if key < p.key:
                                p.left = r
                                r.parent = p
                            else:
                                p.right = r
                                r.parent = p
                        else:
                            if key < p.key:
                                p.left = None
                            else:
                                p.right = None
                else:
                    if l != None:
                        while max.right != None:
                            max = max.right
                        pre = max.parent
                        if max.left != None:
                            self.root.key = max.key
                            pre.right = max.left
                            max.left.parent = pre
                            max = None
                        else:
                            self.root.key = max.key
                            pre.right = None
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

b.delete(2)
b.print()
print(b.size)

b.delete(22)
b.print()
print(b.size)