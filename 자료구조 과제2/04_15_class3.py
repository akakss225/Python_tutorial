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
        
    def preOrder(self, n):
        print(n.item,' ', end=' ')
        if n.left: self.preOrder(n.left)
        if n.right: self.preOrder(n.right)
    
    def inOrder(self, n):
        if n.left: self.inOrder(n.left)
        print(n.item,' ', end=' ')
        if n.right: self.inOrder(n.right)

    def postOrder(self, n):
        if n.left: self.postOrder(n.left)
        if n.right: self.postOrder(n.right)    
        print(n.item,' ', end=' ')

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

a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)
c.setLeft(f)
c.setRight(g)
d.setLeft(h)
e.setLeft(i)
e.setRight(j)
g.setRight(k)

bt = BinaryTree(a)
bt.preOrder(a)
print()
bt.inOrder(a)
print()
bt.postOrder(a)