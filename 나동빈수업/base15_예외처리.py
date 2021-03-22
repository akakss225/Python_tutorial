'''
try:
    print(3 /0)
except:
    print('0으로는 나눌 수 없습니다.)

즉, 예외 가능성이 있는 코드가 try에 들어가고,
예외가 발생할 경우 except에 들어간 코드가 출력이 된다.
'''
try:
    print(3/0)
except:
    print('0으로는 나눌 수 없습니다.')

# else를 넣음으로써 디테일 추가 가능.
try:
    print(3/2)
except:
    print('0으로는 나눌 수 없습니다.')
else:
    print('예외 없이 성공적으로 실행되었습니다.')

# finally를 넣어 무조건적으로 출력하는 구문을 만들 수 있다.
try:
    print(3/0)
except:
    print('0으로는 나눌 수 없습니다.')
else:
    print('예외 없이 성공적으로 실행되었습니다.')
finally:
    print('예외 처리를 마칩니다.')

# 파이썬이 기본적으로 제공하는 Exception을 사용해서 오류메세지를 직접 출력가능
try:
    print(3/0)
except Exception as e:
    print(e)
else:
    print('예외 없이 성공적으로 실행되었습니다.')
finally:
    print('예외 처리를 마칩니다.')