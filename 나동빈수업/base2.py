# 이차원 list
a = [
    [90, 95, 83, 40, 30, 20, 19, 48, 39, 59],
    [48, 53, 64, 76, 58, 34, 55, 85, 96, 85]
]
sum = 0
english = a[0]
for i in english:
    sum = sum + i
print("영어 평균 점수 : ", sum/len(english))

sum = 0
math = a[1]
for i in math:
    sum = sum + i
print("수학 평균 점수 : ",sum/len(math))
