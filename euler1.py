

x3=3
tmpsum3=0
while (x3 < 1000):
    tmpsum3+=x3
    x3+=3

x5=5
tmpsum5=0
while (x5 < 1000):
    tmpsum5+=x5
    x5+=5
    
x15=15
tmpsum15=0
while (x15 < 1000):
    tmpsum15+=x15
    x15+=15
    
endsum=tmpsum3+tmpsum5-tmpsum15
print(endsum)
