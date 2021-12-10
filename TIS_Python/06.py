# 12 / 10 (fri) class 5 . 랜덤 + 그래프

import matplotlib.pyplot as plt
import random

dice = []

for i in range(1000000):
    dice.append(random.randint(1,6))
plt.hist(dice, bins=6)
plt.show()
