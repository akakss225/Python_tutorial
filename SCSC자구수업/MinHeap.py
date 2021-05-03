# 최소 힙(Min heap)
import numpy as np

class MinHeap:
    def __init__(self):
        self.h = []
        
    def size(self):
        return len(self.h)
    
    def height(self):
        height = 0
        start = 0
        while self.has_L_child(start):
            start = self.get_L_child(start)
            height += 1
        return height
    
    def get_level(self, idx):
        level = 0
        while self.has_parent(idx):
            idx = self.get_parent(idx)
            level += 1
        return level
        
    def find_min(self):
        return self.h[0]
    
    def get_parent(self, idx):
        return (idx - 1) // 2
    
    def get_L_child(self, idx):
        return idx * 2 + 1
    
    def get_R_child(self, idx):
        return idx * 2 + 2
    
    def has_parent(self, idx):
        if idx == 0:
            return False
        else:
            return self.get_parent(idx) >= 0
            
    def has_L_child(self, idx):
        return self.get_L_child(idx) < self.size()
    
    def has_R_child(self, idx):
        return self.get_R_child(idx) < self.size()
    
    def swap(self, a, b):
        self.h[a] , self.h[b] = self.h[b] , self.h[a]
    
    def heapify_up(self, idx):
        if self.has_parent(idx):
            t = self.get_parent(idx)
            while t >= 0:
                if self.has_R_child(t):
                    if self.h[self.get_R_child(t)] < self.h[self.get_L_child(t)]:
                        if self.h[self.get_R_child(t)] < self.h[t]:
                            self.swap(self.get_R_child(t), t)
                    else:
                        if self.h[self.get_L_child(t)] < self.h[t]:
                            self.swap(self.get_L_child(t), t)
                else:
                    if self.h[self.get_L_child(t)] < self.h[t]:
                        self.swap(self.get_L_child(t), t)
                t -= 1
                
    def heapify_down(self, idx):
        while self.has_L_child(idx) or self.has_R_child(idx):
            if self.has_R_child(idx):
                if self.h[self.get_L_child(idx)] > self.h[self.get_R_child(idx)]:
                    if self.h[idx] > self.h[self.get_R_child(idx)]:
                        self.swap(idx, self.get_R_child(idx))
                        idx = self.get_R_child(idx)
                else:
                    if self.h[idx] > self.h[self.get_L_child(idx)]:
                        self.swap(idx, self.get_L_child(idx))
                        idx = self.get_L_child(idx)
            else:
                if self.h[idx] > self.h[self.get_L_child(idx)]:
                        self.swap(idx, self.get_L_child(idx))
                        idx = self.get_L_child(idx)
                        
                    
    def insert(self, key):
        self.h.append(key)
        self.heapify_up(self.h.index(key))
        
    def delete(self):
        self.swap(0, self.size()-1)
        temp = self.h.pop()
        self.heapify_down(0)
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
h.delete()
print(h.h)