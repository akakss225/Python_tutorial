import re
p = re.compile('[a-z]+')
m = p.match('python')
n = p.match('3 python')
print(m)
print(n)