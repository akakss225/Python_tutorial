#튜플형태로 함수를 만들면, 두개 이상의 값이 한번에 나타낼 수 있다.

def Calculating(a,b):
    return a+b,a-b,a*b,a/b

#인덱스를 이용해 골라서 값을 출력할 수 있다. << 중요

print(Calculating(1,2))
print(Calculating(1,2)[0])
print(Calculating(1,2)[1])
