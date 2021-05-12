# 위키피디아 데이터 엑셀로 저장하기
import pandas as pd

# 헤더를 열 이름으로 지정하고, 나라 이름을 인덱스 이름으로 지정하는 속성 추가
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0) # 웹 페이지의 테이블 형태 데이터 불러오기

print(df[1])
