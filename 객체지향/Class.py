#반복되는 변수 혹은 메소드를 미리 정해놓은 틀에 넣은것.
#일종의 설계도이다.

result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
#만일 다른 두개의 합을 계산하는 식을 짜고 싶다고 가정한다면,
#클래스를 사용하지 않으면 위의 코드처럼 '중복'이 들어간다.
#따라서 클래스를 만들면 중복을 없앨 수 있다.

class Calculator :
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
        
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
