
f = open('out.txt',"w")
for x in range(0,4096):
    f.write(str(x))
    f.write('  ')
    f.write(hex(x))
    f.write('\n')

f.close()

