f = open('score.txt', 'w')

for i in range(0,5):
    score = int(input('점수를 입력해 주세요'))
    data = '%d\n'%score
    f.write(data)
    print()

f.close()