# bmi 지수 구하기(bmi : 몸무게 / 키(M)^2)
# 함수이름 : Bmi_Calculator
# 변수이름 : Height, Weight, bmi

def Bmi_Calculator(Height, Weight):
    bmi = Weight / Height**2
    return bmi

print(Bmi_Calculator(1.78, 72))
