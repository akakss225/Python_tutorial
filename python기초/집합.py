#수학의 집합 개념과 동일하다. 중복불가.
#주로 데이터를 다룰 때 중복된것을 출력해야하거나, 빼야할 때 사용.

#s1 = set([1,2,3])
s1 = {1,2,3}

print(type(s1))
print(s1)

l = [1,2,2,3,3]
newList = list(set(l))

print(type(newList))
print(newList)
