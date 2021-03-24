f = open('score.txt', 'r')

list = [0]*5
for i in range(0,5):
    list[i] = int(f.readline())
    print(list)


print(sum(list))
print(sum(list)/5)

f.close()

    