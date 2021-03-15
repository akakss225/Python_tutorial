a = [1,2,3]

b = a
a[1] = 4

print(a)
print(b)

#주소값이 같기 때문에 a의 인덱스를 바꿔도 b가 바뀜.
print(id(a))
print(id(b))
print(a is b)#같은 주소 혹은 같은 값을 갖는지 물어보는 문법

