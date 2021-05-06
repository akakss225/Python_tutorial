import numpy as np
import csv

a = [[],[],[],[],[],[],[]]

with open('/Users/sumin/Desktop/Python/Python_tutorial/컴퓨팅사고 과제/passby_data.CSV', 'r') as f:
    reader = csv.DictReader(f)
    i = j = 0
    for row in reader:
        a[i].append(row)
        j += 1
        if j % 24 == 0:
            i += 1

x_title = ['MON', 'TUE', 'WED', 'THR', 'FRI','SAT', 'SUN']

for i in range(7):
    for j in range(len(a[i])):
        print(x_title[i], '[',j,'] =',a[i][j])

# 일별 제목
day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']

# 시간대 제목
hour_title = ['01', '02','03', '04', '05', '06', \
              '07', '08','09', '10', '11', '12', \
              '13', '14','15', '16', '17', '18', \
              '19', '20','21', '22', '23', '24',]
# avgh(average hour) : 시간대별로 주간 평균 구하는 리스트 
avgh = [ ]

# (실습) 각 시간대(0~23)의 모든 요일의 유동인구(num)의 합 구하기
for j in range(  0,24  ):
  day_sum = 0
  # (실습) 각 시간대의 모든 요일(0~6)의 유동인구의 합 구하기
  for i in range( 0,7  ):
    # (실습) a[i][j]['num']에 저장된 값을 누적합 계산하기 
    day_sum = day_sum + int(a[i][j]['num'] )
  # print(day_sum)
  # 각 시간대 모든요일 유동인구 합 평균 구하기 
  avgh.append(day_sum/7)
  

# 시간대별 평균 유동 인구 출력하기
# format 형식 {인덱스:길이 또는 채우기}
print(" 시간대별 평균 유동 인구 출력하기 ")
for j in range (0, 24) :
    print("[~{0}:00]:{1:4}".format(hour_title[j], int(avgh[j])))

