# 이진탐색트리 (Binary Search Tree)
# 각 노드의 왼쪽 subtree의 key값은 노드의 key값보다 작거나 같아야하고,
# 각 노드의 오른쪽 subtree의 key값은 노드의 key값보다 커야한다.
# 이진탐색트리의 경우, key값을 search 할 때 매우 유용하다(특정 값을 찾을 때 루트부터 시작해서 모든 노드에서 절반씩 잘라서 확인 가능). O(h)



class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = self.left = self.right = None
        
    def __str__(self):
        return str(self.key)


class BST: # Binary Search Tree
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    
    def find_loc(self, key): # 찾고자하는 key값이 존재하면, 그 자리를 return하고, 없다면, 그 key값이 삽입이 될 부모노드를 return한다.
        if self.size == 0:
            return None
        else:
            v = self.root
            p = None
            while v != None:
                if v.key == key:
                    return v
                elif v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
            return p
        
    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v
        
    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= v.key:
                    p.left = v
                else:
                    p.rigjt = v
            self.size += 1
            return v
        else:
            print('Key is already in tree')
            return p
        

a = BST()
a.insert(15)
a.insert(4)
a.insert(20)
a.insert(12)
a.insert(2)
a.insert(17)
a.insert(19)
a.insert(32)