# 균형이진탐색트리 (Balanced BST) _ 정의와 회전
# 기본적으로 힙구조의 이진탐색트리는 데이터를 search하는데에 그 의미가 있다. (각 레벨당 1번씩의 비교만으로 시간을 단축시킬 수 있는것임)
# 균형이진탐색트리의 경우 n개의 노드가 저장된 BST에서 그 트리의 높이가 log(n)에 비례하게 항상 유지시켜주는 것을 말한다.
# AVL 트리 
# Red-Black 트리
# 2,3,4 트리
# Splay 트리
# 일정 높이 이상으로 넘어가면, rotation즉, 회전을 시켜서 높이를 줄여준다.
# right rotation , left rotation


class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

    def preOrder(self):
        if self.key != None:
            print(self.key,end=" ")
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    
    def inOrder(self):
        if self.key != None:
            if self.left:
                self.left.inOrder()
            print(self.key, end=" ")
            if self.right:
                self.right.inOrder()

class BBST:
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    def find(self, key):
        if self.size == 0:
            print('Tree is empmty')
        else:
            preNode = None
            curNode = self.root
            if curNode.key == key:
                return curNode
            else:
                while curNode != None:
                    if curNode.key < key:
                        preNode = curNode
                        curNode = curNode.right
                    elif curNode.key == key:
                        return curNode
                    else:
                        preNode = curNode
                        curNode = curNode.left
                return preNode
        
    def insert(self, key):
        newNode = Node(key)
        if self.size == 0:
            self.root = newNode
        else:
            preNode = self.find(key)
            if preNode.key < key:
                preNode.right = newNode
                newNode.parent = preNode
            elif preNode.key == key:
                print('key값이 이미 존재합니다.')
            else:
                preNode.left = newNode
                newNode.parent = preNode
        self.size += 1
    
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
                print('key is not exist')
            else:
                if p != None:
                    if l != None:
                        if p.key < key:
                            l.parent = p
                            p.right = l
                            while m.right != None:
                                m = m.right
                            if r != None:
                                m.right = r
                                r.parent = m
                            else:
                                m.right = None
                        else:
                            l.parent = p
                            p.left = l
                            while m.right != None:
                                m = m.right
                            if r != None:
                                m.right = r
                                r.parent = m
                            else:
                                m.right = None
                    else:
                        if r != None:
                            if key < p.key:
                                r.parent = p
                                p.left = r
                            else:
                                r.parent = p
                                p.right = r
                        else:
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
                
    def rotation_r(self, key):
        if self.size == 0:
            return None
        else:
            z = self.find(key)
            if z == None:
                return
            else:
                p = z.parent
                x = z.left
                b = x.right
                if p != None:
                    if x != None:
                        if key < p.key:
                            p.left = x
                            x.parent = p
                            z.parent = x
                            x.right = z
                            if b != None:
                                z.left = b
                                b.parent = z
                            else:
                                return
                        else:
                            p.right = x
                            x.parent = p
                            z.parent = x
                            x.right = z
                            if b != None:
                                z.left = b
                                b.parent = z
                            else:
                                return
                    else:
                        return
                else:
                    if x != None:
                        self.root = x
                        self.root.right = z
                        z.parent = self.root
                        if b != None:
                            z.left = b
                            b.parent = z
                        else:
                            return
                    else:
                        return
        
    def rotation_l(self, key):
        if self.size == 0:
            return None
        else:
            z = self.find(key)
            y = z.right
            p = z.parent
            b = y.left
            if z == None:
                return
            else:
                if p != None:
                    if y != None:
                        if p.key < key:
                            p.right = y
                            y.parent = p
                            y.left = z
                            z.parent = y
                            if b != None:
                                z.right = b
                                b.parent = z
                            else:
                                return
                        else:
                            p.left = y
                            y.parent = p
                            y.left = z
                            z.parent = y
                            if b != None:
                                z.right = b
                                b.parent = z
                            else:
                                return
                    else:
                        return
                else:
                    if y != None:
                        self.root = y
                        y.left = z
                        z.parent= y
                        if b != None:
                            z.right = b
                            b.parent = z
                        else:
                            return
                    else:
                        return
            
    def print_pre(self):
        self.root.preOrder()
        print()
    
    def print_in(self):
        self.root.inOrder()
        print()
                
        

t = BBST()
t.insert(2)
t.insert(1)
t.insert(3)
t.insert(10)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(8)
t.insert(9)
t.insert(4)
t.insert(11)
t.insert(12)
t.insert(13)
t.insert(14)
t.insert(15)
t.insert(16)
t.insert(17)
t.insert(18)
t.insert(19)

t.print_pre()
t.print_in()
t.delete(19)
t.print_pre()
t.print_in()
t.rotation_r(9)
t.print_pre()
t.print_in()
