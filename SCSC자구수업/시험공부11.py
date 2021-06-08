# MinHeap(tree)

# 1. heapq 라이브러리 >> 기본구조가 minheap
# 2. 직접 구현


import heapq

# h = []
# heapq.heappush(h,15)
# heapq.heappush(h,4)
# heapq.heappush(h,1)
# heapq.heappush(h,6)
# heapq.heappush(h,33)
# heapq.heappush(h,23)
# heapq.heappush(h,13)
# heapq.heappush(h,20)
# heapq.heappush(h,11)
# heapq.heappush(h,3)
# print(h)
# heapq.heappop(h)
# print(h)






class MinHeap:
    def __init__(self):
        self.h = []
        
    def size(self):
        return len(self.h)
    
    def swap(self, a, b):
        self.h[a], self.h[b] = self.h[b], self.h[a]
    
    def getLchild(self, index):
        return index * 2 + 1
        
    def getRchild(self, index):
        return index * 2 + 2
    
    def getParent(self, index):
        return (index - 1) // 2
    
    def hasLchild(self, index):
        if self.size() < self.getLchild(index):
            return False
        else:
            return True
    
    def hasRchild(self, index):
        return self.getRchild(index) < self.size()
    
    def hasParent(self, index):
        if index == 0:
            return False
        else:
            return self.getParent(index) >= 0
        
    def heapifyUp(self, index):
        if self.hasParent(index):
            parent = self.getParent(index)
            while parent >= 0:
                if self.hasRchild(parent):
                    if self.h[self.getLchild(parent)] < self.h[self.getRchild(parent)]:
                        if self.h[self.getLchild(parent)] < self.h[parent]:
                            self.swap(self.getLchild(parent), parent)
                    else:
                        if self.h[self.getRchild(parent)] < self.h[parent]:
                            self.swap(self.getRchild(parent), parent)
                else:
                    if self.h[self.getLchild(parent)] < self.h[parent]:
                        self.swap(self.getLchild(parent), parent)
                parent -= 1

    def insert(self, item):
        self.h.append(item)
        self.heapifyUp(self.h.index(item))
        
    def height(self):
        height = 0
        start = 0
        while self.hasLchild(start):
            start = self.getLchild(start)
            height += 1
        return height
    
    def delete(self):
        self.swap(0, self.size()-1)
        temp = self.h.pop()
        self.heapifyUp(self.size()-1)
        return temp
    
            
            
h = MinHeap()
h.insert(29)
h.insert(14)
h.insert(4)
h.insert(3)
h.insert(46)
h.insert(34)
h.insert(5)
h.insert(16)
h.insert(28)
h.insert(6)
h.insert(9)
h.insert(2)
h.insert(1)
h.insert(33)
h.insert(41)
h.insert(20)
h.insert(13)
h.insert(12)
print(h.h)

h.delete()
print(h.h)