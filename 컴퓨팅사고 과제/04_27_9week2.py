import matplotlib.pyplot as plt

x1 = [1,3,4,5,6,7,9]
y1 = [4,7,2,4,7,8,3]

x2 = [2,4,6,8,10]
y2 = [5,6,2,6,2]

plt.bar(x1, y1, label="Blue Bar", color='b')
plt.bar(x2, y2, label="Green Bar", color='g')
plt.plot()

plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title('Bar Chart Example')
plt.legend()
plt.show()
