class BT:
    def __init__(self):
        self.t = [None]
    
    def append(self, item):
        self.t.append(item)
    
    def size(self):
        return len(self.t) - 1
    
    def level(self, item):
        num = 0
        temp = self.t.index(item)
        while temp != 1:
            temp = temp//2
            num += 1
        return num
    
    def getChild(self, item):
        if item in self.t:
            temp = self.t.index(item)
            lindex = 2 * temp 
            rindex = 2 * temp + 1
            
            if lindex <= self.size():
                left = self.t[lindex]
            else:
                return None
            if rindex <= self.size():
                right = self.t[rindex]
            else:
                return None
            
            return left, right
        else:
            print('item is not found')
            
    def getParent(self, item):
        if item in self.t:
            temp = self.t.index(item)
            parent = temp // 2
            
            if parent > 0:
                return self.t[parent]
            else:
                return None
        else:
            print('item is not found')
    
    def distance(self, a, b):
        if a in self.t and b in self.t: 
            if self.level(a) == self.level(b):
                distance = 0
                a_idx = self.t.index(a)
                b_idx = self.t.index(b)
                while True:
                    if self.t[a_idx] != self.t[b_idx]:
                        a_idx = a_idx // 2
                        b_idx = b_idx // 2
                        distance += 1
                    else:
                        print(distance,'/',self.level(self.t[self.size()]))
                        break
                
t = BT()
t.append('호흡기/소화기병')
t.append('호흡기병')
t.append('소화기병')
t.append('호흡기감염')
t.append('폐질환')
t.append('위질환')
t.append('결장질환')
t.append('독감')
t.append('기관지염')
t.append('폐부종')
t.append('폐색전증')
t.append('위궤양')
t.append('위암')
t.append('대장염')
t.append('대장암')

print(t.getChild('호흡기/소화기병'))
print(t.getChild('호흡기병'))
print(t.getChild('소화기병'))
print(t.level('대장암'))
print(t.distance('대장암', '독감'))