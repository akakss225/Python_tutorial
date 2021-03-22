# 튜플의 원소는 바꿀 수 없지만, 리스트를 원소로써 넣어 다차원 배열처럼 만들 수 있다.

tuple1 = (1,2,3,4,5,6,7,8,9,0)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]

tuple2 = (list1, list2)

print(tuple1)
print(tuple2)

#그렇다면, 이 list의 원소를 바꾸어 튜플의 원소 내용또한 바꿀 수 있다.

list1.append(6)
list2.pop(0)

print(tuple1)
print(tuple2)

