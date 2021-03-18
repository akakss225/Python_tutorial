#Lambda

#def add(a,b):
#    return a+b

#아래의 lambda는 위에 정의된 함수와 같은 의미를 나타낸다.
add = lambda a, b : a+b

print(add(1,2))

#람다는 리스트에 넣을 수 있다.

myList = [lambda a, b : a+b, lambda a, b : a*b]
print(myList[0](1,2))
print(myList[1](2,3))
