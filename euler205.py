#!/bin/env python3
import time
import sys
from numba import njit
import random

@njit
def Roll4s(n=9):
    dsum = 0
    for x in range(n): 
        dsum += random.randint(1,4)
    return dsum

@njit
def Roll6s(n=6):
    dsum = 0
    for x in range(n): 
        dsum += random.randint(1,6)
    return dsum

@njit
def trials(n=100):
    wins=0
    for x in range(n):
        d6=Roll6s()
        d4=Roll4s()
        if d4>d6: wins+=1
    return(wins)

if __name__ == '__main__':

    N = 10000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    start = time.time()
    wins = trials(N)
    print("Trials:",N,"Wins:",wins,"Probability:",wins/N)
    end = time.time()
    print("Elapsed Time:",end - start)



    
