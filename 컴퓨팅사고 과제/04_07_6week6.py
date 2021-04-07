class Circle:
    
    def __init__(self, radius):
        self.radius =radius
        
    def size(self):
        area = 3.14 * self.radius**2
        print('반지름 :', self.radius,'\n넓이 :', area)
    
    def line(self):
        size = 2 * 3.14 * self.radius
        print('반지름 :',self.radius,'\n둘레 :',size)

c1 = Circle(4)
c1.size()
c1.line()
