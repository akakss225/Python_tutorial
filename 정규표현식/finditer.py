import re

p = re.compile('[a-z]+')

m = p.findall('python')
n = p.findall('3 python')
l = p.findall('life is too short')

#일치하는 문자열을 리스트 형태로 출력해줌!
print(m)
print(n)
print(l)

#finditer는 match되는 문자열을 전부 match객체 형태로 출력시켜준다.
for i in l:
    print(i)
