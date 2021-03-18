# IGNORECASE, I

import re

p = re.compile('[a-z]')
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

# 대,소문자 구분 필요 x
q = re.compile('[a-z]',re.I)
print(q.match('python'))
print(q.match('Python'))
print(q.match('PYTHON'))