
import numpy as np

rows = 6
columns = 7
# ar = np.arange(1,row*column+1).reshape(row,column)
# x1, y1, x2, y2 = [2,2,5,4] - 1
# print(x1, y1, x2, y2)
# print(ar)

procession = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i*columns+j + 1)
    procession.append(row)

print(procession)

x1 = 1
y1 = 1
x2 = 4
y2 = 3
cordinate = []
for j in range(x1, x2+1):
    cordinate.append([j, y1])
for j in range(y1+1, y2+1):
    cordinate.append([x2, j])
for j in range(x2-1, x1-1, -1):
    cordinate.append([j, y2])
for j in range(y2-1, y1, -1):
    cordinate.append([x1, j])
        
print(cordinate)