#a를 완전 복제해서 새로운 b를 만드는 방법

a = [1,2,3]

b = a[:] #슬라이싱 후 넣으면 바뀌는것임!

a[1] = 4

#주소가 달라짐.
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)