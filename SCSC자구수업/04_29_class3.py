# 최소 힙(Min heap)

class MinHeap:
    def __init__(self):
        self.h = []
    
    def getParent(self, idx):
        return idx // 2
    
    def getLchild(self, idx):
        return idx * 2 + 1
    
    def getRchild(self, idx):
        return idx * 2 + 2
    
    def hasParent(self, idx):
        return self.getParent(idx) != None
    
    def hasLchild(self, idx):
        return self.getLchild(idx) < len(self.h)
    
    def hasRchild(self, idx):
        return self.getRchild(idx) < len(self.h)
    
    def swap(self, a, b):
        self.h[a], self.h[b] = self.h[b], self.h[a]
        
    def heapufy_down(self, idx):
        while self.hasLchild(idx) or self.hasRchild(idx):
            if self.h[idx] < self.h[self.getLchild(idx)] or self.h[idx] < self.h[self.getRchild(idx)]:
                if self.h[self.getLchild(idx)] > self.h[self.getRchild(idx)]:
                    self.swap(idx, self.getLchild(idx))
                    idx = self.getLchild(idx)
                else:
                    self.swap(idx, self.getRchild(idx))
                    idx = self.getRchild(idx)
            
    def insert(self, key):
        self.h.append(key)
        self.heapufy_down(0)
        
    def getMin(self):
        return self.h[0]
    
    def delete_Min(self):
        self.h.pop(0)
        self.heapufy_down(0)
        
    
        
        


h = MinHeap()
h.insert(12)
h.insert(2)
h.insert(15)
h.insert(6)
h.insert(11)
h.insert(10)
h.insert(3)
h.insert(1)
h.insert(9)
h.insert(8)
print(h.h)

h.delete_Min()
print(h.h)

