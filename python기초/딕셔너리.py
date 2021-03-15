##일종의 사전이다.##
##자바의 Map이랑 같은 개념.##
##Key와 Value로 이루어져있어, key를 입력하면 value가 나오는 형식이다.##
##리스트는 순서가 중요할때, 딕셔너리는 정보가 중요할때 사용할수도??##
##key는 중복이 불가.##

a = {1 : 'a'}
a['name'] = "익명"


print(a)
print(a['name'])

del a[1]
print(a)

b = {1 : '송수민', 2 : '김민', 3 : '김석주'}

print(b.keys())
print(b.values())
print(b.items())
for k in b.keys():
    print(k)

for v in b.values():
    print(v)

for k,v in b.items():
    print("키는: " ,str(k))
    print("벨류는: " ,v)

b.clear()

print(b)