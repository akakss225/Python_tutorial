#기존에 사용하던 함수에서도 입 출력값에 따른 출력이 달라짐을 이제 이해할 수 있다.
#다양한 예제


myList = [1,2,3]

print(myList.append(4))

print(myList.pop())

def say():
    print('Hi')

print(say())
say()

def sum_many(*args):# *args는 파이썬에서 '몇개든 상관없다'를 의미한다.
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_many(1,2,3))