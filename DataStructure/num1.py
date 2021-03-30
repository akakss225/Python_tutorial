# 자료구조 리스트
'''
x = [1,2,3,4,5]
y = ['hello', 'world']

print(x.index(3))
print(y.index('hello'))

print(10 in x) # 리스트 내부에 자료가 존재하는지물어보는 문법

if 'hello' in y:
    print('hello가 있습니다.')

'''
# 자료구조 튜플
'''
a = (1,2,3,4,5)
b = ('a', 'b', 'c')
c = (1,'hello', 'there')

print(a + b)
print('a' in b)
print(c.index(1))
'''
# 자료구조 딕셔너리

# key값에는 불변하는 자료만 넣는다.
'''
x = {
    'name' : 'sumin',
    'age' : 27
}
y = {
    0 : 'Hello',
    1 : 'world'
}

print(x['name'])
print(x['age'])
print(y[0])
print(y[1])

print(x.keys())
print(x.values())

print(y.keys())
print(y.values())

for key in x:
    print('key :' ,key)
    print('value :',x[key])

y[1] = 'sumin'

print(y.values())

x['school'] = '인하'

print(x)
'''

# 간단한 자료짜기


fruit = ['사과', '사과', '바나나', '바나나', '딸기', '키위', '복숭아','복숭아', '복숭아']
'''
what = input('어떤 과일의 갯수를 알고싶으십니까 :')

num = 0

for i in range(len(fruit)):
    if what == fruit[i]:        
        num += 1 

print(num)
'''

d = {}

for f in fruit:
    if f in d:
        d[f] += 1
    else:
        d[f] = 1
print(d)
