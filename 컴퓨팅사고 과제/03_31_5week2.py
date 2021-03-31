# 버블정렬

def bubleSort(value):
    for i in range(len(value)):
        for j in range(1,len(value)-i):
            if value[j-1] > value[j]:
                temp = value[j-1]
                value[j-1] = value[j]
                value[j] = temp
        print('step',i,'-',value)

a =[50, 6, 77, 11, 43]
print(a)
print(bubleSort(a))
