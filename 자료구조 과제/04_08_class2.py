# Stack and Queue

# Queue(Queuing Theory) : First in / First out

# 커피가게 rotaiton

import numpy as np
import matplotlib.pyplot as plt
lamda = 1
x = np.linspace(0, 10,100)
pdf = (1/lamda) * np.exp(-x/lamda)
plt.plot(x,pdf)
plt.show()