def getTotalPage(m, n):
    if m % n != 0:
        return m // n + 1
    else:
        return m // n

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(31, 10))