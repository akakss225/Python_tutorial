# 객체와 클래스 << 객체지향이란??

class Cookie:
    count = 0
    def __init__(self, ingredient, sugar_gram):
        self.ingredient = ingredient
        self.sugar_gram = sugar_gram
        Cookie.count += 1
    
    def print(self):
        print(Cookie.count,'번째 쿠키','\n재료 :',self.ingredient,'\n설탕 :',self.sugar_gram,'g\n')
        
        
cookie1 = Cookie('초코', 30)
cookie1.print()

cookie2 = Cookie('딸기', 20)
cookie2.print()

cookie3 = Cookie('바나나', 35)
cookie3.print()