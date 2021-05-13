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

class BBST:
    def __init__(self):
        self.root = None()
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
                        curNode = curNode.left
                    elif curNode.key == key:
                        return curNode
                    else:
                        preNode = curNode
                        curNode = curNode.right
                return preNode
        