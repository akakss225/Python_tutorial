'''
<H.W # 8> 싸다싸 쇼핑몰에서는 마우스 재고를 항상 10개 보유하고 있다.
마우스는 최저가 마우스만 팔린다고 가정하고 하나가 팔리면 곧 바로 하나가 재고가 보충된다. 
마우스 한개의 도입가격은 7,000원이고 마우스 판매 가격은 평균 만원, 표준편차 천원인 정규분포를 따른다고 가정할 때, 
마우스 한개당 평균 이익은 얼마인가? 예: 9,200원에 마우스를 팔면 이익은 2,200원이다.
'''
import numpy as np

class MinHeap:
    def __init__(self):
        self.h = []
        
    def size(self):
        return len(self.h)
    
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
        while (self.has_parent(idx) and self.h[idx] < self.h[self.get_parent(idx)]):
            self.swap(idx, self.get_parent(idx))
            idx = self.get_parent(idx)
            
    def insert(self, key):
        self.h.append(key)
        self.heapify_up(self.h.index(key))



h = MinHeap()
h.insert(10)
h.insert(2)
h.insert(15)
h.insert(30)
h.insert(41)
h.insert(12)
h.insert(25)
h.insert(27)
h.insert(3)
h.insert(1)
h.insert(9)
print(h.has_parent(0))
print(h.h)