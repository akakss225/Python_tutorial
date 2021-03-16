class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class MoreFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return -1
        else :
            return self.first / self.second

a = MoreFourCal(4,0)
print(a.add())
print(a.div())