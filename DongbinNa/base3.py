a = [10, 20, 30, 40, 50, 10, 20]
b = [20, 30, 40, 50, 60, 20, 30]

print(a)
print(a.count(10))
print(a.index(50))
a.append(25)
print(a)
a.sort()
print(a)
a.extend(b)
print(a)
a.insert(3, 70)
print(a)
a.remove(10) # 가장 앞에서 발견되는 특정 원수 삭제
print(a)
a.pop(5) # 이는 특정 인덱스의 원소를 삭제
print(a)
a.reverse()
print(a)