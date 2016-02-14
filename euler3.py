
import math as math
import numpy as np
prime=600851475143
np.set_printoptions(precision=100)
#Pollard's rho algorithm for factorization can be implemented as:
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)


def factorPR(n):
    for slow in [2,3,4,6]:
        numsteps=2*math.floor(math.sqrt(math.sqrt(n))); fast=slow; i=1
        while i<numsteps:
            slow = (slow*slow + 1) % n
            i = i + 1
            fast = (fast*fast + 1) % n
            fast = (fast*fast + 1) % n
            g = gcd(fast-slow,n)
            if (g != 1):
                if (g == n):
                    break # try a new base
                else:
                    return g
    return 1 # fail to factor

#def factors(n):    
#    return set(reduce(list.__add__,  ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

x=[]

x = factors(prime)
print(x)

print(np.argsort(x))

for z in x:
    print(z)
    print(factors(z))
    print()
