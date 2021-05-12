import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.rand(8,3), index=index,columns=list('ABC'))
print(df)

print(df['B']) # 특정 열의 데이터만을 볼 수 있음.

print(df['B'] > 0.4) # 마스크 생성하기. 이는 내가 원하는 데이터만을 사용하기에 용이하게 해준다.

df2 = df[df['B'] > 0.4] # 마스크 생성 후, 원하는 데이터만을 테이블 형태로 출력하는 예시.
print(df2)

print(df.T) # 행과 열을 바꿔주기

df['D'] = df['A'] / df['B'] # 행 별로 계산이 되어 D에 추가됨.
print(df)
