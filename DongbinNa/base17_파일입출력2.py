# open() : 파일을 특정한 모드로 여는 함수.
# read() 파일 객체로부터 모든 내용을 읽는 함수.

f = open('input.txt', 'r', encoding='UTF-8')

data = f.read()
print(data)
f.close()
