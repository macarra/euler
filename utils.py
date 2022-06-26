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