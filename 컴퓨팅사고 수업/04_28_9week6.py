import matplotlib.pyplot as plt

def my_sum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

def my_avg(a):
    return my_sum(a)/len(a)


x_data = ['MON','TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
a = [232, 258, 232, 221, 270, 81, 47]

plt.title('Floating Population Data(1week)', fontsize=18)

plt.xlabel("Day of the week", fontsize=12)
plt.ylabel("Floating Population", fontsize=12)

plt.scatter(x_data,a)

plt.plot(x_data, a)

print(my_sum(a))
print(my_avg(a))

plt.show()
