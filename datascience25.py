# -*- coding: utf-8 -*-
"""DataScience25

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YD-WPxHruMLxmLQc_ma3xjVWaz9d8TQh
"""

import numpy as np
distance = [20, 40 , 80, 120, 200, 300]
time = [15, 30, 60, 90, 120, 150]
distances = np.array(distance)
times = np.array(time)
speed = distances / times
print(speed)

value = [20, 40 , 80, 120, 200, 300]
qty = [15, 30, 60, 90, 120, 150]
values= np.array(value)
qtys=np.array(qty)
price=values/qtys
print(price)

import matplotlib.pyplot as plt
plt.plot([1,2,3,2,5, 7, 8])
plt.ylabel('number')
plt.xlabel('materils covered')

import numpy as np
import matplotlib.pyplot as plt
returns = np.random.normal(0.01, 0.02, 250)
initial_price =100
price = initial_price*np.exp(returns.cumsum())
plt.plot(price)
plt.grid()

