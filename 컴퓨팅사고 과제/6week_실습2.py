# 간단한 게임 캐릭터 및 몬스터 짜기
class Monster:
    def __init__(self, name, power = None, hp = None, mp = None):
        if name == '슬라임':
            self.name = name
            self.power = 5
            self.hp = 15
            self.mp = 0
        elif name == '식인거미':
            self.name = name
            self.power = 10
            self.hp = 25
            self.mp = 0
        elif name == '플랜트':
            self.name = name
            self.power = 3
            self.hp = 60
            self.mp = 0
    
    def attack(self, user):
        if self.name == '슬라임':
            print('슬라임의 공격으로',user.name,'의 체력이 5 감소하였습니다.')
            user.hp -= 5
        elif self.name == '식인거미':
            print('식인거미의 공격으로',user.name,'의 체력이 10 감소하였습니다.')
            user.hp -= 10
        elif self.name == '플랜트':
            print('플랜트의 공격으로',user.name,'의 체력이 3 감소하였습니다.')
            user.hp -= 3
    
    def status(self):
        if self.hp <= 0:
            return None
        print('캐리터명 :',self.name)
        print('공격력 :',self.power)
        print('HP :',self.hp)
        print('MP :',self.mp)


class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.XP = 0
        self.power = 7
        self.hp = 30
        self.mp = 15
        self.Cl = None
        
    def attack(self,monster):
        if self.level == 1:
            print(self.name,'의 공격이',monster.name,'에게 적중해',self.power,'만큼의 데미지를 입혔습니다.')
            monster.hp -= self.power
            if monster.hp <= 0:
                print(monster.name,'을 처치했습니다.')
                if monster.name == '슬라임':
                    self.XP += 10
                elif monster.name == '식인거미':
                    self.XP += 20
                else:
                    self.XP += 25
    
    def status(self):
        print('캐리터명 :',self.name)
        print('직업 :',self.Cl)
        print('경험치 :',self.XP)
        print('공격력 :',self.power)
        print('HP :',self.hp)
        print('MP :',self.mp)
        

user1 = Character('수민')

slime = Monster('슬라임')
spider = Monster('식인거미')
plant = Monster('플랜트')
slime.status()
user1.status()
user1.attack(slime)
slime.status()
user1.attack(slime)
slime.status()
user1.attack(slime)
slime.status()

user1.status()