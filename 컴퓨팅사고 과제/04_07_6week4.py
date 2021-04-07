# 은행 계좌 관리 프로그램

# 입력 : 입금 혹은 출금할 금액을 입력받는다.
# 처리사항 : 입금 및 출금을 진행하여 계좌의 잔액을 갱신한다.
# 출력 : 입금 및 출금 상태와 잔액을 출력해야한다 / 예금 조뢰 시 잔액을 출력해야 한다.

class Account:   
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #입금메소드
    def deposit(self, amount):
        self.balance += amount
        print(self.name,'계좌에', amount,'원 입금, 잔액 :',self.balance)
    
    #출금 메소드
    def withdraw(self, amount):
        self.balance -= amount
        print(self.name,'계좌에', amount,'원 출금, 잔액 :',self.balance)
        
    #예금 조회 메소드
    def prbalance(self):
        print(self.name,'님 계좌 잔액은',self.balance,'원 입니다.')

John = Account('John', 100)
John.deposit(100)
John.withdraw(250)
John.deposit(200)
John.withdraw(200)
John.prbalance()
