
import math as math
import numpy as np
import time
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

pcheck = isprime(10)
pnum=2
prime=3
s=time.time()
while (pnum < 10001):
    prime+=2
    pcheck = isprime(prime)
    if pcheck:
        pnum+=1
        print pnum, prime

print time.time() - s
print prime
#104743
