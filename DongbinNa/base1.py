# List

x = int(input('학생의 수를 입력해주세요 : '))
students = []

for i in range(0,x):
    students.append(0)
print(students)

for i in range(0,x):
    a = float(input('%d번째 학생의 학점을 입력해주세요 : '%(i+1)))
    students[i] = a
    print(students)

for i in range(0,x):
    if students[i] < 1.7:
        print("%s번째 학생은 낙제입니다." %(i + 1))
    else :
        print("%s번째 학생은 합격입니다." %(i + 1))
