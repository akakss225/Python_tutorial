# Tree
# 이진트리 : 자식 node가 무조건 두개 이하인 Tree
# 자식이 없는 노드를 단말노드라고 한다.
# 노드가 n 개이면 간선은 n-1개이다.
# 높이가 h인 노드의 수 최소값은 h+1이고, 최대값은 2**(h+1) -1이다.
# 높이가 h인 이진트리에서 최대노드를 가지는 트리를 포화이진트리라고 한다.
# 포화이진트리에서 노드가 몇개 빠진트리를 완전이진트리라고 한다.
# 편향이진트리는 한쪽으로만 자식노드가 존재하는 트리를 말한다. << 트리의 장점이 아니므로, 리스트로만드는게 더 좋다
# 부모인덱스는 왼쪽자식 인덱스 /2 , 오른쪽자식 인덱스 /2 + 1의 값을 갖는다.


class BinaruTree:
    def __init__(self):
        self.t = [None]
    
    def append(self, item):
        self.t.append(item)
    
    def size(self):
        return len(self.t)-1
    
    def getChild(self, item):
        if item in self.t:
            k = self.t.index(item)
            lidx = 2 * k
            ridx = 2 * k + 1
            if lidx <= self.size():
                lnode = self.t[lidx]
            else:
                lnode = None
            if ridx <= self.size():
                rnode = self.t[ridx]
            else:
                rnode = None    
            return lnode, rnode
        else:
            print('item not found~')
    
    def getParent(self, item):
        if item in self.t:
            k = self.t.index(item)
            pidx = k // 2
            if pidx > 0:
                return self.t[pidx]
            else:
                return None
        else:
            print('item not found~')

t = BinaruTree()

for i in range(12):
    t.append(chr(65+i))

print(t.t)
print(t.getChild('C'))

      