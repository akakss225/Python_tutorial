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
# 1d = {'사과' : 1}
# 2d = {'사과' : 2}
# 3d = {'사과' : 2, '바나나' : 1} 사이클이 돌때마다 이런식으로 증가...

for f in fruit:
    # f = '사과'
    
    if f in d: # '사과'라는 key가 딕셔너리 d에 들어있어?
        d[f] += 1 # 그럼 '사과' 갯수를 하나 늘려줘
    else: # 없으면
        d[f] = 1 # '사과'라는 값을 넣고, 그 값을 1로 지정해줘.
        # 즉, for - if 구문을 한번 돌때마다, key가 추가되거나, value값이 재설정 된다.
        
print(d)
