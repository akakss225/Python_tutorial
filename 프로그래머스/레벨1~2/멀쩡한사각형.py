def gcd(w, h):
    if w < h:
        w, h = h, w
    while h != 0:
        n = w % h
        w = h
        h = n
    return w


def solution(w,h):
    return (w * h) - (w + h) + gcd(w,h)

w = 8
h = 12

# w h
# 8 12 80
# 7 12 66
# 6 12 60
# 5 12 45
# 4 12 36

# 80
print(solution(w,h))