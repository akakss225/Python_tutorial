# 인류 최초의 알고리즘 : 최대공약수 계산.

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

print(gcd(8,12))
