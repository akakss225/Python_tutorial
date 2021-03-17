f = open('None.txt', "w")

try:
    #무언가 수행
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    #열려있는 파일을 보호하기 위함.
    f.close()
