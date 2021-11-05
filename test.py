import math

def nums(n):
    result = 0
    for i in range(1, n+1):
        result += int(math.pow(3,i))
    return result

def threepow(n):
    count = 1
    while True:
        if nums(count) >= n:
            return count
        else:
            count += 1
    
print(threepow(39))
# 1 0 2
# # 11 > 42
# 1 1 0
# # 12 > 44
# 1 1 1
# # 13 > 111
# 1 1 2
# # 14 > 112
# 1 2 0
# # 15 > 114
# 1 2 1 
# # 16 > 121
# 1 2 2
# # 17 > 122
# 2 0 0
# # 18 > 124
# 2 0 1
# # 19 > 141
# 2 0 2
# # 20 > 142
# 2 1 0
# # 21 > 144