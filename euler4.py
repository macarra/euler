
import math as math
import numpy as np

isPali = lambda num: str(num) == str(num)[::-1]

xlist=[]
for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        if isPali(num):
            xlist.append(num)
            
sortlist = np.argsort(xlist)
print xlist[sortlist[-1]]
