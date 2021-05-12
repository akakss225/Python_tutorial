# 테이블 형태의 데이터를 쉽게 다루도록 도와주는 pandas
# series : 1차원 배열 형태의 데이터 구조
# DataFrame : 2차원 배열 형태의 데이터 구조

# DataFrame 기초

import pandas as pd

index = pd.date_range('1/1/2000', periods=8)

print(index)