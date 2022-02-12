from macutils import *

maxnum=10000
d=[]
pairs =[] 
d.append(0)
for index in range(1,maxnum):
    dvsum = [int(x) for x in get_divisors(index)]
    dvsum.remove(index)
    dvsum=sum(dvsum)
    d.append(dvsum)
    #print(index,d[index])

pairset = set()
for index in range(1,maxnum):
    try:
        if index == d[d[index]]:
            if not index==d[index]:  
                print(index,d[index],d[d[index]])
                pairs.append([index,d[index]])
                pairset = pairset.union(set([index,d[index]]))
    except Exception:
        pass
print(pairs)
print(pairset)
print(sum(pairset))


