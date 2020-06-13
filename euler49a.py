
import math as math
import numpy as np

def isprime(number):  
    if number<=1 or number%2==0:  
        return 0  
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return 0  
        check+=2  
    return 1  

x=[]
for i in range(1000,10000):
    if isprime(i):
        x.append(i)

print(len(x))


def numlist(z):
    xlist=[]
    x1=int(z/1000)
    xlist.append(x1)
    x2=int((z-x1*1000)/100)
    xlist.append(x2)
    x3=int((z-x1*1000-x2*100)/10)
    xlist.append(x3)
    x4=z-x1*1000-x2*100-x3*10
    
    sorted=np.argsort(x)
    xnum=sorted[0]
    print("xnum",xnum)

z=4529
print( numlist(z))
