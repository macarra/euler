#!/usr/bin/env python
# coding: utf-8

# 
# 
# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# 


def buildString(max):
    text = ''
    for i in range(1,max+1):
        text+=str(i)
    return text
buildString(12)


def getVal(n):
    text = buildString(n)
    return text[n-1]
getVal(5)


def getMul(dvals):
    mul=1
    for i in dvals:
        val = getVal(i)
        #print(i,val)
        mul *= int(val)
    return mul


if __name__ == '__main__':

    dvals = [1,10,100,1000,10000,100000,1000000]
    result = getMul(dvals)
    print(result)




