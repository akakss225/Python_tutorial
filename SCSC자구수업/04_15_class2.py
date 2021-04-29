# LinkedList를 이용한 Tree

class BNode:
    def __init__(self, item):
        self.item=item
        self.left = None
        self.right = None
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node   

class BinaryTree:
    def __init__(self,root):
        self.root = root

a = BNode('A')
b = BNode('B')
c = BNode('C')
d = BNode('D')
e = BNode('E')
f = BNode('F')
g = BNode('G')
h = BNode('H')
i = BNode('I')
j = BNode('J')
k = BNode('K')
l = BNode('L')

a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)
c.setLeft(f)
c.setRight(g)
d.setLeft(h)
d.setRight(i)
e.setLeft(j)
e.setRight(k)
f.setLeft(l)

t = BinaryTree(a)

print(t)