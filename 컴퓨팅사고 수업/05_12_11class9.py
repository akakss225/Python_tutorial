import pandas as pd

# 리스트 형태로 pd구현

data = [['1000', 'Steve', 90.72],
        ['1001', 'James', 78.09],
        ['1002', 'Doyeon', 98.43],
        ['1003', 'Jane', 64.19],
        ['1004', 'Pilwoong', 81.30],
        ['1005', 'Tony', 99.14]
        ]
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)

# 딕셔너리 형태로 pd구현

data2 = {'학번':['1000','1001','1002','1003','1004','1005'],
         '이름':['Steve','James','Doyeon','Jane','Pilwoong','Tony'],
         '점수':[90.72,78.09,98.43,64.19,81.30,99.14]}

df2 = pd.DataFrame(data2)
print(df2)

# 앞 부분 세개만 데이터 출력
print(df.head(3))
# 뒷 부분 세개만 데이터 출력
print(df.tail(3))
# 학번 열만 추출
print(df['학번'])

# 외부의 데이터 읽기
df3 = pd.read_excel('/Users/sumin/Desktop/Python/하계올림픽메달.xlsx')
print(df3)