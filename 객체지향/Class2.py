class FourCal:
# init의 경우 class를 인스턴스화 할 때 가장 먼저 수행되는 메소드이다.
#    def __init__(self, first, second):
#        self.first  = first
#        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result


a = FourCal()
a.setdata(1,2)
print(a.first)
print(a.second)
print(a.add())
print(a.minus())
