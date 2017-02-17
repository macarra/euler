def printOUT(nbnum,answer):
    f=open('answers.txt','a')
    outstr = "Euler" + str(nbnum) + ": " + str(sum) + "\n"
    f.write(outstr)
    f.close()
