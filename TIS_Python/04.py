# 12 / 10 (fri) class 4 . 크롤링(파싱)

import csv
f = open("seoul2.csv", "r")

data = csv.reader(f)


next(data) # 첫번째 행을 건너뜀


max_temp = -999
max_date = ""

for row in data:
    if row[-1] == "":
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]
f.close()

print("서울의 기온이 가장 높았던 때는 ", max_date, "이며, ", max_temp, "도 였습니다.")

