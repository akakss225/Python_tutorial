# MULTILINE, M
import re
# ^는 맨 처음이라는 표현(맨 처음에 python이라는 단어를)
# \s는 공백을 나타냄
# \w는 단어를 나타냄
p = re.compile('^python\s\w+')

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

q = re.compile('^python\s\w+',re.M)

print(q.findall(data))