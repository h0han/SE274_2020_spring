import time
import matplotlib.pyplot as plt
import math
import random
from skiplist import SkipList

SL = SkipList()
start=time.time()
x_axis=[]
y_axis=[]
for i in range(10000):
    key = random.randrange(10000)
    value = 1
    SL[key] = value
    last_key = key
    if(i%10==0):
        x_axis.append(i)
        y_axis.append(time.time() - start)
        start=time.time()

plt.plot(x_axis,y_axis)
plt.show()