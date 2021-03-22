# 쉬운 함수의 경우 람다식을 이용해 매우 간결하게 만들 수 있음.

add = lambda x, y: x + y

print(add(1,2))

# map() : 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 있도록 도와줌
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

my_function = lambda a, b : a +b
result = map(my_function, list1, list2)
print(result) # 오브젝트 생성.
print(list(result)) # 출력은 리스트식으로 가능.

