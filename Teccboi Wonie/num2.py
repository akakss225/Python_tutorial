# 간단한 class 만들기.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self, to_name):
        print('안녕!', to_name,' 나는', self.name)

    def introduce(self):
        print('안녕 나는',self.name,'내 나이는',self.age,' 살이야')

# introduce 메소드를 오버라이딩.
class Police(Person):
    def arrest(self, to_arrest):
        print('넌 체포됐다,', to_arrest)
    def introduce(self):
        print('안녕 나는',self.name,'내 나이는',self.age,' 살이야', '그리고 나는 police야')
        
class Programmer(Person):
    def program(self, to_program):
        print('다음엔 뭘 만들지? 아 이걸 만들어야겠다', to_program)
    def introduce(self):
        print('안녕 나는',self.name,'내 나이는',self.age,' 살이야', '그리고 나는 programmer야')

sumin = Person("수민",27)
seokjoo = Police("석주",24)
kimmin = Programmer("민",25)

sumin.say_hello('철수')
seokjoo.say_hello('영희')
kimmin.say_hello('기철')

sumin.introduce()
seokjoo.introduce()
kimmin.introduce()

seokjoo.arrest('조두순')
kimmin.program('게임')
