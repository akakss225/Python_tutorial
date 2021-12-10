# 12 / 10 (fri) class 3 . 크롤링(파싱)

import csv
f = open("seoul.csv", "r")

data = csv.reader(f)


next(data) # 첫번째 행을 건너뜀


max_temp = -999
max_date = ""

for row in data:
    if row[4] == "":
        row[4] = -999
    row[4] = float(row[4])
    if max_temp < row[4]:
        max_date = row[2]
        max_temp = row[4]
f.close()

print("서울의 기온이 가장 높았던 때는 ", max_date, "이며, ", max_temp, "도 였습니다.")
