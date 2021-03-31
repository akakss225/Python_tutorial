def calc_area(r):
    area = 3.14 * r * r
    return area

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

r = 5

print(calc_area(r))
print(factorial(r))
print(sum(1,10))


