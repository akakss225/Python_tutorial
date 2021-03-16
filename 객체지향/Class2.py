class FourCal:
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
