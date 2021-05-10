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
            temp_c = self.find(key)
            temp_p = temp_c.parent
            temp_l = temp_c.left
            temp_r = temp_c.right
            temp_m = temp_l
            if temp_p.key != key:
                return None
            else:
                if temp_p != None:
                    if temp_c.key < temp_p.key:
                        if temp_l != None:
                            temp_c = temp_l
                            temp_c.parent = temp_p
                            temp_p.left = temp_c
                            while temp_m != None:
                                temp_m = temp_m.right
                            if temp_r != None:
                                temp_m.right = temp_r
                                temp_r.parent = temp_m
                        else:
                            temp_c = temp_r
                            temp_c.parent = temp_p
                            temp_p.left = temp_c
                    else:
                        if temp_l != None:
                            temp_c = temp_l
                            temp_c.parent = temp_p
                            temp_p.right = temp_c
                            while temp_m != None:
                                temp_m = temp_m.right
                            if temp_r != None:
                                temp_m.right = temp_r
                                temp_r.parent = temp_m
                        else:
                            temp_c = temp_r
                            temp_c.parent = temp_p
                            temp_p.left = temp_c
                else:
                    if temp_l != None:
                        temp_c = temp_l
                        while temp_m != None:
                            temp_m = temp_m.right
                        if temp_r != None:
                            temp_m.right = temp_r
                            temp_r.parent = temp_m
                    else:
                        temp_c = temp_r
                        temp_c.parent = temp_p
                        temp_p.left = temp_c
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