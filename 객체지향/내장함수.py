#파이썬에 기본적으로 포함된 함수. (print, type 등)
print(abs(-3))# abs는 절댓값 함수.

def positive(x):
    return x > 0

a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)
