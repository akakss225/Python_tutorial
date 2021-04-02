# 삽입정렬

def insertionSort(value):
    for i in range(len(value)):
        j = i
        temp = value[i]
        while value[j-1] > temp and j > 0:
            value[j] = value[j-1]
            j -= 1
        value[j] = temp
        print('step',i,'-',value)
a = [50, 6, 77, 11, 43]

print(a)
print(insertionSort(a))

