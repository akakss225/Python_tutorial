# BMI 계산 및, 25이상일 경우 과체중표시.

def BMI(height, weight):
    bmi = round(weight / height **2,2)
    if bmi > 25:
        print('BMI =',bmi,'과체중 입니다.')
    elif bmi > 27:
        print('BMI =',bmi,'비만 입니다.')
    else:
        print('BMI =',bmi,'표준 입니다.')

print(BMI(1.78, 72.9))
print(BMI(1.83,88.1))
