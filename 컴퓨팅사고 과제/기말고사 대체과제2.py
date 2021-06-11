import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np



# 탄수화물이 장내 미생물에 끼치는 영향을 Bacteriodetes에는 1, Firmicutes에도 1 의 가중치를 대입
# 단백질이 장내 미생물에 끼치는 영향을 Bacteriodetes에는 3, Firmicutes에는 1.5의 가중치를 대입
# 지방이 장내 미생물에 끼치는 영향을 Bacteriodetes에는 1.5, Firmicutes에는 3의 가중치를 대입
# 약 3년(1000일)동안 특정 식단을 진행한 후 각각 늘어나는 Microbiome에 따라 평균을 내고, 그래프화 해 추이를 확인한다.
# 여기서 기준치를 잡기 위해 평균섭취는 10, 고섭취는 12, 저섭취는 8으로 잡는다.
# 또한 가장 실제를 투영해주기 위해 표준편차는 각각 2씩 잡아준다.






# f1 = open('Diet.csv','w')
# w = csv.writer(f1)
# w.writerow(['/', 'Carbon', 'Protein', 'Fat'])
# for i in range(1000):
#     w.writerow([i, np.random.normal(10, 2), np.random.normal(12, 2), np.random.normal(8, 2)])

f = open('Diet2.csv','r')
data = csv.reader(f)
person2 = []
for i in data:
    person2.append(i)



def judgment(person):
    carbon = [1, 1]
    protein = [3, 1.5]
    fat = [1.5, 3]
    bacterio = 0
    firmicutes = 0
    normal = 0
    
    for i in range(1, 1000):
        normal += (float(person[i][1]) * 3) + (float(person[i][2]) * 3) + (float(person[i][3]) * 3)
        bacterio += (float(person[i][1]) * carbon[0]) + (float(person[i][2]) * protein[0]) + (float(person[i][3]) * fat[0])
        firmicutes += (float(person[i][1]) * carbon[1]) + (float(person[i][2]) * protein[1]) + (float(person[i][3]) * fat[1])
    
    x1 = [bacterio]
    x2 = [firmicutes]
    x3 = [normal]
    
    plt.figure(figsize=[15, 10])
    X = np.arange(len(x1))
    
    plt.bar(X, normal, color = 'b', width = 0.25)
    plt.bar(X + 0.25, bacterio, color = 'g', width = 0.25)
    plt.bar(X + 0.5, firmicutes, color = 'r', width = 0.25)
    
    plt.legend(['Normal', 'Bacteriodetes', 'Firmicutes'])
    plt.xticks([i + 0.25 for i in range(1)], ['Person1'])
    plt.title("Rumen MicroBiome")
    plt.ylabel('% of Microorganism')
    plt.savefig('Person2.png')
    plt.show()
    
judgment(person2)