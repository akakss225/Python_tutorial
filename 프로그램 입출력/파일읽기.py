f = open("새파일.txt","r")
line = f.readline()
print(line)
f.close()

while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()