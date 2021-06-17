# 간단한 재귀함수 예제 feat Factorial

def factorial_iter(i):
    result = 1
    if i == 0 or i == 1:
        return result
    for n in range(1, i + 1):
        result *= n
    return result
    

def factorial_recul(i):
    if i <= 1:
        return 1
    else:
        return i * factorial_recul(i - 1)
    

i = 5
print(factorial_iter(i))
print(factorial_recul(i))

# 간단한 재귀함수 예제2 feat 유클리드 호제법 << 자연수 두개의 최대 공약수 구하기.
# 이때 자연수 A B에 대하여, A > B이다.
# 유클리드 호제법 : 두 자연수 A, B가 있을때 A를 B로 나눈 나머지 R에 대하여, B 와 R의 최대공약수와 A와 B의 최대공약수가 같다는 것.


def gcd(A, B):
    if A % B ==  0:
        return B
    else:
        return gcd(B, A % B)
    
print(gcd(192, 162))