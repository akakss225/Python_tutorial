from tkinter import Label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[15, 10])

bacteriodetes = [25, 18]
normal = [60, 55]
firmicutes = [15, 27]


X = np.arange(len(bacteriodetes))

plt.bar(X, normal, color = 'b', width = 0.25)
plt.bar(X + 0.25, bacteriodetes, color = 'g', width = 0.25)
plt.bar(X + 0.5, firmicutes, color = 'r', width = 0.25)

plt.legend(['Normal', 'Bacteriodetes', 'Firmicutes'])
plt.xticks([i + 0.25 for i in range(2)], ['Normal People', 'Obesity'])
plt.title("Rumen MicroBiome")
plt.ylabel('% of Microorganism')
plt.savefig('4BarPlot.png')
plt.show()


