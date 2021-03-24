f = open('score.txt', 'r')

list = [0]*5
for i in range(0,5):
    list[i] = int(f.readline())
    print(list)

data = 0
for i in range(0,5):
    data += list[i]

print(data)
print(data/5)

f.close()

    