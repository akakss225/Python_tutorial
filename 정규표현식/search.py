import re
p = re.compile('[a-z]+')

m = p.search('python')
#match와는 다르게 맞는부분을 찾아서 return해준다.
n = p.search('3 python')

print(m)
print(n)
