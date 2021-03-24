# 별찍기

# 계단

n = int(input('n:'))

for i in range(n):
    print(' '*i,end='')
    print('*'*n)


# 삼각형

m = int(input('m:'))

for i in range(m+1):
    print('*'*i)

for i in range(m+1):
    print(' '*(m-i),end="")
    print('*'*i)

# 역삼각형

k = int(input('k:'))

for i in range(k):
    print('*'*(k-i))

for i in range(k):
    print(' '*i,end='')
    print('*'*(k-i))

# 피라미드

l = int(input('l:'))

for i in range(l):
    print(' '*(l-i-1),end='')
    print('*'*(2 * i + 1))

for i in range(l):
    print(' '*i,end='')
    print('*'*(2 * (l - i) - 1))

