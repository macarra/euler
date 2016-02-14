

val1=1
val2=2
newval = val1+val2
tmpsum=2
while (newval<4000000):
    #print newval
    if (newval%2 == 0):
        #print('***')
        tmpsum+=newval
    val1=val2
    val2=newval
    newval=val1+val2
print()
print(tmpsum)
