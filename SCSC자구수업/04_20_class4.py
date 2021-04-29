# Linked List 를 이용한 Tree
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

class BNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
    
    def setLeft(self, node):
        self.left = node
    
    def setRight(self, node):
        self.right = node
    
class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def preOrder(self, n):
        # 순회 알고리즘.
        # 노드에 먼저 방문을 하고, 좌측먼저 훑으면서 방문하고, 우측을 확인한다.
        print(n.item ,' ',end="")
        if n.left:
            self.preOrder(n.left)
        if n.right:
            self.preOrder(n.right)
        
    
    def inOrder(self, n):
        # 처음부터 방문을 하지 않고, 좌측 맨 끝으로 먼저 이동한다.
        # 이후 돌아오면서 방문한다.
        # 방문이 끝난 노드에서는 우측으로 이동하고, 다시 좌측 끝까지 간다. 이후 돌아오며 방문
        if n.left:
            self.inOrder(n.left)
        print(n.item,' ',end="")
        if n.right:
            self.inOrder(n.right)
    
    def postOrder(self, n):
        # 좌측으로 이동하고, 돌아오며 방문하는데, 우측을 확인 후 돌아오며 방문한다.
        if n.left:
            self.postOrder(n.left)
        if n.right:
            self.postOrder(n.right)
        print(n.item,' ',end="")
        
        

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
t.preOrder(a)
print()
t.inOrder(a)
print()
t.postOrder(a)