import matplotlib.pyplot as plt

def my_sum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

def my_avg(a):
    return my_sum(a)/len(a)

def my_sum_weekday(a):
    sum = 0
    for i in range(len(a)-2):
        sum += a[i]
    return sum

def my_avg_weekday(a):
    return my_sum_weekday(a)/(len(a)-2)


#x축 데이터 저장하기
x_data = ['MON','TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
a = [232, 258, 232, 221, 270, 81, 47]

# 유동인구 제목
plt.title('Floating Population Data(1week)', fontsize=18)

# x축(요일), y축(유동인구수) 정하기
plt.xlabel("Day of the week", fontsize=12)
plt.ylabel("Floating Population", fontsize=12)

# 산점도 그리기(x축 : 요일, y축 : 유동인구수)
plt.scatter(x_data[0:5],a[0:5],c='r',s=50)
plt.scatter(x_data[5:],a[5:],c='b',s=50)


# 라인그래프 그리기
plt.plot(x_data, a)

print(my_sum(a))
print(my_avg(a))
print(my_sum_weekday(a))
print(my_avg_weekday(a))

plt.show()

