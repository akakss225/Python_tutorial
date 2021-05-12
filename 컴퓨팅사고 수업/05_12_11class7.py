# 위키피디아 데이터 엑셀로 저장하기
import pandas as pd

# 헤더를 열 이름으로 지정하고, 나라 이름을 인덱스 이름으로 지정하는 속성 추가
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0) # 웹 페이지의 테이블 형태 데이터 불러오기

#금메달 기준으로 데이터 정렬하기(내림차순)

summer = df[1].iloc[:,:5]
summer.columns = ['경기수', '금', '은', '동', '계'] # 열 이름을 바꿀 수 있음.


print(summer.sort_values('금', ascending=False)) # ascending = False 는 내림차순, True는 오름차순.

# 최종적으로 테이블을 엑셀로 저장하기.

summer.to_excel('하계올림픽메달.xlsx')
