# Tree : 부모 자식간 연결구조를 Tree라고 한다.
# root : 가장 조상의 node
# link, edge : 연결 가지
# leaf : 자식 node가 없는 node
# level : root = level0 / 1세대 = level1 / 2세대 = level2 ...
# higher : root로부터 leaf까지 몇개의 node를 거치느냐, 갯수 레벨의 수와 같다.
# path : 어떠한 node x 에서 node y 까지 가는 경로의 수 출발/ 경유 / 도착
# path length : 경로에 포함되어있는 link의 갯수
# binary tree : 이진트리, 자식을 최대 두개까지만 가질 수 있는 tree, 자식노드중, 왼쪽에는 부모보다 작은 수, 오른쪽에는 부모보다 큰 수가 들어간다.
# 리스트형태로 만들어 줄 때, 왼쪽node가 오른쪽 node보다 먼저 입력된다.
# 포화이진트리 : 모든 node가 꽉 차있는 tree
# 완전이진트리 : 마지막 레벨의 node가 다 채워지지 않은 tree
# 편향이진트리 : 한쪽으로만 치우쳐진 tree
# Heap(힙) : 전부 다 차 있는 상태의 tree라고 가정하고, 비어있는 node는 none 등으로 채운다.

class Node:
    def __init__(self, value):
        self.value = value
        self.llink = None
        self.rlink = None

class Tree:
    def __init__(self):
        self.root = None
        
    def push(self, value):
        newNode = Node(value)
        curNode = self.root
        
        if self.root == None:
            self.root = newNode
            
        while True:
            parent = curNode
            if value < curNode.value:
                curNode = curNode.llink
                if curNode is None:
                    parent.llink = newNode
                    break
            else:
                curNode = curNode.rlink
                if curNode is None:
                    parent.rlink = newNode
                    break

t = Tree()

t.push(6)
t.push(7)
t.push(3)
        