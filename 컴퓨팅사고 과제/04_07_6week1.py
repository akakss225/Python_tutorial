# 객체와 클래스 << 객체지향이란??

class Cookie:
    def __init__(self, ingredient, sugar_gram):
        self.ingredient = ingredient
        self.sugar_gram = sugar_gram
    
    
    
    def print(self):
        print('재료 :',self.ingredient,'\n설탕 :',self.sugar_gram,'g')
        
        
cookie1 = Cookie('초코', 30)
cookie2 = Cookie('딸기', 20)
cookie3 = Cookie('바나나', 35)
cookie1.print()
cookie2.print()
cookie3.print()