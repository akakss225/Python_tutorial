# 12 / 10 (fri) class 5 . 그래프

import matplotlib.pyplot as plt
import csv

# 기온변화를 그래프로 그리기

f = open("seoul2.csv", "r")

data = csv.reader(f)

next(data) # 첫번째 행을 건너뜀
high = []
low = []

for row in data:
    if row[-1] != "" and row[-2] != "":
        date = row[0].split(".")
        if 1995 <= int(date[0]):
            if date[1] == '4' and date[2] == '17':
                high.append(float(row[-1]))
                low.append(float(row[-2]))

f.close()

plt.rcParams["axes.unicode_minus"] = False # 마이너스 기호 깨짐 방지
plt.title("내 생일의 기온 변화 그래프")      # 제목 설정
# high 리스트에 저장된 값을 hotpink 색으로 그리고 레이블을 표시
plt.plot(high, "hotpink", label="high")
# low 리스트에 저장된 값을 skyblue 색으로 그리고 레이블을 표시
plt.plot(low, "skyblue", label="low")
plt.legend()          # 범례 표시
plt.show()            # 그래프 나타내기










