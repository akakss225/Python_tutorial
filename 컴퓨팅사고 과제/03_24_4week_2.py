menu = {'김밥' : 2000, '라면' : 3000, '돈까스' : 6000}

print(menu.keys())
print(menu.values())
print(menu.items())
del menu['김밥']

print(menu.items())

# 세트라고 불림
A = {10,20,30}
B = {30,40}

print(A & B)
print(A | B)
print(A - B)
# 값 추가시 A.add()/ 여러개의 값을 추가시 A.update([,])/ 특정 값 삭제시 A.remove()
A.add(40)
print(A)
B.update([50,60])
print(B)
A.remove(30)
print(A)