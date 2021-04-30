# 높이에 따른 순회 LevelOrder

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
        
    def height(self, n):
        # 특정 노드에서 왼쪽으로 끝까지 가보고, 오른쪽으로 끝까지 가보고 ...
        if n is None:
            return 0
        else:
            lheight = self.height(n.left)
            rheight = self.height(n.right)
            # 각 노드별로 끝이 됐을 때, 리턴값을 프린트한다.
            print(n.item, lheight + 1, rheight + 1)
            # Use the larger one
            # 루트 노드가 맨 마지막에 리턴된다.
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
        
    def levelOrder(self):
        # 루트 노드의 높이를 구한 다음 높이가 1부터 h까지 순차적으로 노드를 구한다.
        h = self.height(self.root)
        for i in range(1, h + 1): # 높이가 1, 2, ... , h 까지 순차적으로 프린트한다.
            self._levelOrder(self.root, i)
            print()

    # 특정 노드의 레벨에 해당하는 노드를 프린트한다.
    # 예: 루트에서 레벨 2를 프린트한다면 레벨을 한 단계 낮춰 루트 좌우로 이동한다.
    # 이후, 레벨 1이 되므로 루트의 좌, 우 노드가 프린트 된다.
    # 루트에서 레벨 3을 프린트 한다면 레벨을 한 단계 낮춘 상태 즉 루트 바로 밑을 루트로 보고 재귀적으로 레벨 2를 수행하는 것이다.

    def _levelOrder(self, node, level):
        if node is None:
            return
        # 특정 노드의 level == 1일 때, 특정 노드 값을 인쇄한다.
        if level == 1:
            print(node.item, end = " ")
        # level > 1 이면 특정 노드의 좌, 우측으로 이동해서 레벨을 다운시켜 진행한다.
        elif level > 1:
            self._levelOrder(node.left, level - 1)
            self._levelOrder(node.right, level - 1)     
            
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

t = BinaryTree(a)
print("\npre-order")
t.preOrder(a)
print("\nin-order")
t.inOrder(a)
print("\npost-order")
t.postOrder(a)
print("\nlevel-order")
t.levelOrder()