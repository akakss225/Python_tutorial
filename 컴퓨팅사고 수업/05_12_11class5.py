# 위키피디아 데이터 엑셀로 저장하기

import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0,index_col=0) # 웹 페이지의 테이블 형태 데이터 불러오기

# 하계 올림픽에 대한 데이터만 추출하기

summer = df[1].iloc[:,:5] # iloc의 경우 데이터의 순서에 따라 접근시키는 것. 중괄호 안 ',' 를 중심으로 앞은 행 뒤는 열을 의미한다.

print(summer)