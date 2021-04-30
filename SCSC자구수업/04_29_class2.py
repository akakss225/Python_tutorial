# Binary Heap
# 최소 힙 : 부모노드가 자식노드보다 작거나 같은 완전 이진 트리
# 최대 힙 : 부모노드는 자식노드보다 커야함

# 이번 수업에선 '최대 힙' 을 만들어 본다.
# 다만 본 수업에서는 원래 힙에서 조금 더 편의를 구하기 위해 0번째 인덱스에 None을 넣어준다.
# heapify_down의 경우 heap에 들어있는 n 개의 갯수만큼의 수행시간을 갖는다 O(n)

# 15 12 6 11 10 2 3 1 8의 숫자를 이용

class MaxHeap:
    def __init__(self):
        self.h = [None]
    
    def size(self):
        return len(self.h)-1
    
    def getParent(self, idx):
        return idx // 2
    
    def getLchild(self, idx):
        return idx * 2

    def getRchild(self, idx):
        return idx * 2 + 1
    
    def hasParent(self, idx):
        return self.getParent(idx) != 0
    
    def hasLchild(self, idx):
        return len(self.h) - 1 > self.getLchild(idx)
    
    def hasRchild(self, idx):
        return len(self.h) - 1 > self.getRchild(idx)
    
    def swap(self, a , b):
        self.h[a] , self.h[b] = self.h[b] , self.h[a]
        
    def heapify_up(self, idx):
        while (self.hasParent(idx) and self.h[idx] > self.h[self.getParent(idx)]):
            self.swap(idx, self.getParent(idx))
            idx = self.getParent(idx)
    
    def insert(self, key):
        self.h.append(key)
        self.heapify_up(self.h.index(key))
        
        
h = MaxHeap()
h.insert(12)
h.insert(2)
h.insert(15)
h.insert(6)
h.insert(11)
h.insert(10)
h.insert(3)
h.insert(1)
h.insert(8)

print(h.h)