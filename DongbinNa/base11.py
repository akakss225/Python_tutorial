dict = {}

dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'Effort'

print(dict)

print(dict['안녕'])

for i, k in enumerate(dict):
    print('[인덱스:',i, '] 한글:', k, '/ 영어:', dict[k])


dict['안녕'] = 'Hi'

print(dict)

if '노력' in dict:
    print('[노력] 키가 존재합니다.')

score = {}

score['송수민'] = 78
score['김민'] = 90
score['김석주'] = 88
score['나호준'] = 59
print(sorted(score)) # 키로 정렬하기
print(sorted(score, reverse=True)) # 내림차순 정렬
print(sorted(score.values())) # 값으로 정렬하기

