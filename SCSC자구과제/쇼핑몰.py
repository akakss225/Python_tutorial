'''
<H.W # 8> 싸다싸 쇼핑몰에서는 마우스 재고를 항상 10개 보유하고 있다.
마우스는 최저가 마우스만 팔린다고 가정하고 하나가 팔리면 곧 바로 하나가 재고가 보충된다. 
마우스 한개의 도입가격은 7,000원이고 마우스 판매 가격은 평균 만원, 표준편차 천원인 정규분포를 따른다고 가정할 때, 
마우스 한개당 평균 이익은 얼마인가? 예: 9,200원에 마우스를 팔면 이익은 2,200원이다.
'''
import numpy as np
import math



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
        if self.has_parent(idx):
            temp = self.get_parent(idx)
            while temp >= 0:
                if self.has_R_child(temp):
                    if self.h[self.get_L_child(temp)] < self.h[self.get_R_child(temp)]:
                        if self.h[self.get_L_child(temp)] < self.h[temp]:
                            self.swap(self.get_L_child(temp), temp)            
                    else:
                        if self.h[self.get_R_child(temp)] < self.h[temp]:
                            self.swap(self.get_R_child(temp), temp)                            
                else:
                    if self.h[self.get_L_child(temp)] < self.h[temp]:
                        self.swap(self.get_L_child(temp), temp)
                temp -= 1

    def insert(self, key):
        self.h.append(key)
        self.heapify_up(self.h.index(key))
        
    def delete(self):
        self.swap(0, self.size()-1)
        temp = self.h.pop()
        self.heapify_up(self.size()-1)
        return temp



h = MinHeap()

# a = np.random.normal(10000,1000,10) 순서대로 평균/ 표준편차 / 사이즈 의미

# 10개의 재고를 유지하면서, 가장 가격이 싼 제품을 담을 list를 생성해놓는다.
result = []
for i in range(1000):
    # 평균이 10000이고, 표준편차가 1000인 임의의 금액을 heap에 넣어준다.
    a = np.random.normal(10000,1000)
    h.insert(round(a))
    print(h.h)
    # 힙의 크기가 10개가 넘어가면, 가장 작은값을 결과에 넣어준다.
    if h.size() > 10:
        # 이때, 이윤의 평균을 구하기위해 원가인 7000원을 뺀 상태로 넣어준다.
        result.append(h.delete() - 7000)

# 리스트 내부 값의 평균을 구하는 mean함수 사용 
profit = np.mean(result)
print(profit) 
