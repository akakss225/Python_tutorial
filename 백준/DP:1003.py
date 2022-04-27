# 피보나치

import sys

input = sys.stdin.readline

zero_one = [["1", "0"], ["0", "1"], ["1", "1"]]

def fibo(n):
    global zero_one
    if n == 1:
        return zero_one[1]
    if n == 2:
        return zero_one[2]
    if n < len(zero_one):
        return zero_one[n]
    
    zero_one.append([str(int(fibo(n-1)[i]) + int(fibo(n-2)[i])) for i in range(2)])
    return zero_one[n]

T = int(input())

rs = []
for i in range(T):
    N = int(input())
    rs.append(fibo(N))

for i in rs:
    print(" ".join(i))


