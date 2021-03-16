f = open("새파일.txt", "a")

for i in range(11,20):
    data = "This is %d line.\n" % i
    f.write(data)
f.close()
