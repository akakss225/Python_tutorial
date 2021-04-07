
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print('안녕하세요\n제 이름은',self.name,'입니다.','\n나이는',self.age,'살 입니다.')

p1 = Person('송수민', 27)

p1.introduce()
