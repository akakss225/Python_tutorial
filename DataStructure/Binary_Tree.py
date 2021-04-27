# 순회방법
# preOrder / inOrder / postOrder
# preOrder : MLR 순서로 방문한다. 즉, 자기자신을 먼저 방문하고, 좌변으로 전부 방문을 하고 마지막에 우측으로 이동한다.
# inOrder : LMR
# postOrder : LRM
# 순회방법을 안다면, 모양을 모르는 이진트리의 모양을 알아낼 수 있다(reconstruct).



class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    
    def preOrder(self): 
        if self.key != None:
            print(self.key, end=" ")
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    
    def inOrder(self):
        if self.key != None:
            if self.left:
                self.left.inOrder()
            print(self.key,end=" ")
            if self.right:
                self.right.inOrder()

    
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.key,end=" ")
    
            
    
    def __str__(self):
        return str(self.key)
    

a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
a.right = c
b.parent = c.parent = a
b.right = d
d.parent = b

a.preOrder()
print()
a.inOrder()
print()
a.postOrder()


