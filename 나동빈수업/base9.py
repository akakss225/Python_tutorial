class Car :
    # 클래스 생성자로써 init을 사용
    def __init__(self, name, color):
        self.name = name
        self.color = color
    # 클래스 소멸자
    def __del__(self):
        print('인스턴스를 소멸시킵니다.')
    # 클래스 메소드
    def show_info(self):
        print('이름:', self.name, '/ 색상:', self.color)
    # Setter 메소드
    def set_name(self, name):
        self.name = name


car1 = Car("소나타", 'red')
car1.show_info()
print(car1.name) # 특정 멤버 변수에도 접근이 가능함.

car2 = Car('아반떼', 'blue')
car2.show_info()
print(car2.name)

car1.set_name('제네시스')
print(car1.name)

del car1
del car2


car1.show_info()
car2.show_info()
