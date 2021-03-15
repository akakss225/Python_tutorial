#문자열의 자료형은 참으로 나타냄.
#빈 문자열은 거짓.
#이런식으로 거의 모든 자료형(튜플, 집합, 리스트 등)에서 빈값은 거짓, 나머진 참으로 본다
#1은 참 0은 거짓 None은 거짓

a = True

if a :
    print(a)

b = "안녕"

if b :
    print(b)

c = ""

if c :
    print(c)

d = [1,2,3,4]

while d :
    d.pop()
    print(d)
    