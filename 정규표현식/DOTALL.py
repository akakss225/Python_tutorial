# DOTALL , S
# 줄바꿈을 해도 인식가능
import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m)

q = re.compile('a.b', re.S)
n = q.match('a\nb')
print(n)
