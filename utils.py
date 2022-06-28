def printOUT(nbnum,answer):
    f=open('answers.txt','a')
    outstr = "Euler" + str(nbnum) + ": " + str(sum) + "\n"
    f.write(outstr)
    f.close()

def printList(alist,cols=6):
    colindex=1
    for item in alist:
        print(item," ",end='')
        if colindex % cols==0:
            print()
        colindex+=1
        
def getUniqueFromList(alist):
    return list(set(alist))


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


def factors(n):
    return set(x for tup in ([i, n//i] 
               for i in range(1, int(n**0.5)+1) if n % i == 0) 
                                for x in tup)
