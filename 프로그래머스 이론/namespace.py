# namespace는 이름관리를 위한 dictionary container이다.
# 모든 class, instance, function은 자신의 namespace를 갖는다.

a = 2020
b = a
c = a
a = 3000
print(a,b,c)
