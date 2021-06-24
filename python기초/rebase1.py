dic = {'Kor': 80,'Eng' : 90,'Math' : 77}

print(dic.items())

dic['Bio'] = 100

print(dic.items())

if 'Bio' in dic:
    print('생물학 시험을 치뤘습니다.')
else:
    print('생물학 시험을 치루지 않았습니다.')

d = dict()

d['Bio'] = 100

print(d.items())