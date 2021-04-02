# 클래스 상속!
# 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(self.name, '이(가) 공격을 수행합니다. [ 전투력:', self.power, "]")
    
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def show_info(self):
        print('몬스터 이름:', self.name, '/ 몬스터 종류', self.type)

unit = Unit('홍길동', 375)
unit.attack()


monster = Monster('슬라임', 10,'초급')
monster.show_info()
monster.attack()

