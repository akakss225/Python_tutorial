# 계좌 관리 클래스
'''
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(self.name,'계좌에', amount,'원 입금, 잔액 :',self.balance)
    
    def withdraw(self, amount):
        self.balance -= amount
        print(self.name,'계좌에', amount,'원 출금, 잔액 :',self.balance)
    
    def check(self):
        print(self.name,'님 현재 계좌잔액은',self.balance,'원 입니다.')
        
p1 = Account('송수민', 200)
p1.check()
p1.deposit(300)
p1.check()
p1.withdraw(600)
'''
# 성적관리 클래스

class Student:
    _kor = None
    _math = None
    _eng = None
    
    def __init__(self, name):
        self.name = name
        
    def getGrade(self, kor, math, eng):
        self._kor = kor
        self._math  = math
        self._eng = eng
    
    def getSum(self):
        sum = self._kor + self._math + self._eng
        print(self.name,'학생의 총점은',sum,'입니다.')
        
    def getAvg(self):
        avg = self._kor + self._math + self._eng / 3
        print(self.name,'학생의 평균은',round(avg,2),'입니다.')
    
    def print(self):
        print(self.name)
        print('국어 :',self._kor)
        print('수학 :',self._math)
        print('영어 :',self._eng)
                
s1 = Student('수민')
s1.getGrade(95,90,85)
s1.print()
s1.getSum()
s1.getAvg()