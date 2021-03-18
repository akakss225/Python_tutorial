import re
p = re.compile('[a-z]+')

m = p.search('python')
n = p.search('3 python')

print(m)
print(n)
