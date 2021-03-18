import re

p = re.compile('[a-z]+')

m = p.findall('python')
n = p.findall('3 python')
l = p.findall('life is too short')

#일치하는 문자열을 리스트 형태로 출력해줌!
print(m)
print(n)
print(l)

for i in l:
    print(i)
