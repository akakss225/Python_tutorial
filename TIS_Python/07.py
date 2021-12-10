# 12 / 10 (fri) class 5 . 기온 + 박스plot

import matplotlib.pyplot as plt
import csv

f = open("seoul2.csv", "r")

data = csv.reader(f)

next(data) # 첫번째 행을 건너뜀
result = []

for row in data:
    if row[-1] != "":
        result.append(float(row[-1]))
f.close()

plt.boxplot(result)
plt.show()