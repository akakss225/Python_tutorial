# 객체와 클래스 << 객체지향이란??

class Cookie:
    count = 0
    def __init__(self, ingredient, sugar_gram):
        self.ingredient = ingredient
        self.sugar_gram = sugar_gram
        Cookie.count += 1
    
    def print(self):
        print(Cookie.count,'번째 쿠키','\n재료 :',self.ingredient,'\n설탕 :',self.sugar_gram,'g')

class Macaron(Cookie):
    butter = 50
    
    def check(self):
        if self.sugar_gram < 50:
            print('마카롱을 만들기엔 설탕 함량이',50-self.sugar_gram,'g 부족합니다.\n' )
        else:
            print(self.ingredient,'마카롱을 만들기에 충분한 재료입니다.\n')
        
cookie1 = Macaron('초코', 30)
cookie1.print()
cookie1.check()

cookie2 = Macaron('딸기', 20)
cookie2.print()
cookie2.check()

cookie3 = Macaron('바나나', 50)
cookie3.print()
cookie3.check()

