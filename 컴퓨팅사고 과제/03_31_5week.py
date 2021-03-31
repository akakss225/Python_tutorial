# 자료구조
# Queue : 선입선출의 구조.
# Stack : 후입선출의 구조.


def selectionSort(value):
    length = len(value)
    for i in range(length - 1):
        indexMin = i
        for j in range(i, length):
            if value[indexMin] > value[j]:
                indexMin = j
        value[i], value[indexMin] = value[indexMin], value[i]
        print('step',i,'-',value)

a = [3,6,4,5,2,1,9,8,7]

print(a)
print(selectionSort(a))
