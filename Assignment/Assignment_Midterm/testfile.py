import time
import matplotlib.pyplot as plt
import math
import random
from skiplist import SkipList

SL = SkipList()
start=time.time()
xList=[]
yList=[]
for i in range(100000):
    key = random.randrange(1000000)
    value = 1
    # print(f'Adding L[{key}] = {value}')
    SL[key] = value
    last_key = key
    if(i%10000==0):
        xList.append(i)
        yList.append(time.time()-start)
        start=time.time()


plt.plot(xList,yList)
plt.show()