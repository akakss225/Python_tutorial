marks = [90, 25, 67, 45, 80]
number = 0
max = []

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)

number2 = 0

for mark2 in marks:
    number2 += 1
    if mark2 < 60:
        continue
    else :
        print("%d학생 축하합니다. 합격입니다." %number2)
