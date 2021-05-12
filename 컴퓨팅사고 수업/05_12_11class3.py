# 위키피디아 데이터 엑셀로 저장하기

import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table') # 웹 페이지의 테이블 형태 데이터 불러오기

 # print(df) # 이 상태로 불러오면 가독성이 떨어짐.
 
print(df[1]) # 인덱싱을 해주면, 가독성이 올라감.
