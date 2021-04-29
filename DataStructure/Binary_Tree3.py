# 삭제연산은 두가지 방법이 존재 1. Merging/ 2. Copying
# Merging : 특정 key값을 찾아 지우는것
#          지정된 값을 지우고, node의 LTree를 가져와서 붙힌다.
#          이후 원래의 RTree를 대치된 node의 RightChild의 자식으로 붙힌다.
# 즉, Merging의 경우, 특정 node를 지우면, 그 node의 leftSubTree를 그 노드 자리에 그대로 붙햐주고,
# 그 이후에 원래 지우기 전 node의 rightSubTree를 새로 붙혀준 SubTree의 가장 큰값(이 경우 무조건 맨 오른쪽 아래의 node가 됨)의 rightSubTree로 붙혀준다.


class Node:
    def __init__(self, item = None):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    def find_loc(self, item): # 찾고자하는 key값이 존재하면, 그 자리를 return하고, 없다면, 그 key값이 삽입이 될 부모노드를 return한다.
        if self.size == 0:
            return None
        else:
            v = self.root
            p = None
            while v != None:
                if v.item == item:
                    return v
                elif v.item < item:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
            return p
        
    def insert(self, item):
        p = self.find_loc(item)
        if p == None or p.item != item:
            v = Node(item)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.item >= v.item:
                    p.left = v
                else:
                    p.rigjt = v
            self.size += 1
            return v
        else:
            print('Key is already in tree')
            return p
    
    # 특정 아이템을 지우면, 지우고 난 후에도 Tree의 형태를 유지해야하기 때문에 메소드 구현시 고려해야한다.
    def deleteByMerging(self, item):
        if self.size == 0: # 비어있는 트리일 경우 None을 return
            return None
        else: # 트리가 비어있지 않으면 진행한다
            
            # 삭제가 될 node
            tmp_x = self.find_loc(item)
            # 삭제가 될 node의 부모
            tmp_p = tmp_x.parent
            # 삭제가 될 node의 왼쪽 자식
            tmp_l = tmp_x.left
            # 삭제가 될 node의 오른쪽 자식
            tmp_r = tmp_x.right
            # 대체된 SubTree에서 가장 큰 값이 들어갈 그릇
            tmp_m = tmp_l
            
            if tmp_x.item != item: # 즉 삭제될 값이 트리 내부에 없는 경우 None을 return해줌
                return None
            else: # 삭제 될 값이 트리 내부에 존재할 경우 진행
                
                if tmp_x.parent != None: # 삭제 될 값이 루트가 아닌 경우
                    if tmp_l != None: # 삭제 될 node의 왼쪽 자식이 있는 경우
                        tmp_x = tmp_l # 삭제될 자리에 왼쪽 자식을 넣어줌
                        tmp_p.right = tmp_x
                        tmp_x.parent = tmp_p
                        while tmp_m.right != None: # 이후에 대체 된 SubTree에서 가장 큰 값을 찾음
                            tmp_m = tmp_m.right 
                        if tmp_r != None: # 삭제 될 node의 원래 오른쪽 자식 node가 None이 아닌경우
                            tmp_r.parent = tmp_m # 오른쪽 자식 node의 부모를 대체된 값의 Max값에 연결해줌
                            tmp_m.right = tmp_r # 마찬가지로 연결해줌
                    else: # 삭제 될 node의 왼쪽 자식이 없는 경우
                        tmp_x = tmp_r # 삭제 될 node에 자리에 그대로 오른쪽 자식을 넣어줌
                        tmp_p.right = tmp_x # 이후 대체된 node를 이전 부모에 연결해줌
                        tmp_x.parent = tmp_p # 마찬가지로 연결해줌
                else:
                    if tmp_l != None:
                        self.root = tmp_l
                        while tmp_m.right != None:
                            tmp_m = tmp_m.right
                        if tmp_r != None:
                            tmp_r.parent = tmp_m
                            tmp_m.right = tmp_r
                    else:
                        tmp_x = tmp_r
                        tmp_p.right = tmp_x
                        tmp_x.parent = tmp_p
        self.size -= 1


t = BST()
t_list = list(t)

t.insert(15)    
t.insert(21)    
t.insert(24)    
t.insert(53)    
t.insert(7)    
t.insert(10)    
t.insert(5)    
t.insert(4)    
t.insert(11)    
t.insert(32)    
t.insert(27)

print(t.size)


t.deleteByMerging(15)
print(t.size)