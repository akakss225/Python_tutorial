# group() : 매치된 문자열을 리턴
# start() : 매치된 문자열의 시작 위치를 리턴
# end() : 매치된 문자열의 끝 위치를 리턴
# span() ; 매치된 문자열의 (시작 , 끝) 에 해당되는 '튜플'을 리턴

import re

p = re.compile('[a-z]+')
m = p.match('python')

print(m.group())
print(m.start())#첫번째 인덱스
print(m.end())#끝 인덱스
print(m.span())#튜플형태

