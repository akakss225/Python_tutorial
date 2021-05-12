# 판다스 테스트 2

import pandas as pd

sr = pd.Series([17000, 18000, 1000, 5000], index=['피자', '치킨', '콜라', '맥주'])

print(sr)
print(sr.values)
print(sr.index)

values = [[1,2,3],[4,5,6],[7,8,9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns= columns) # 값, 인덱스, 열 의 내용을 담는다. 이는 반드시 기억.
print(df)
print(df.index)
print(df.values)
print(df.columns)