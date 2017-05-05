import sys

clean = input()
viral = input()

foundStart = False
foundEnd = False
start = 0
end = 0
n = len(viral)


while not( foundStart and foundEnd):
    s = start
    e = -1 - end  # indexing
    #print('s:%d, e:%d'%(start,end))
    if len(viral) - 1 - end <= start or len(clean) - 1 - end <= start:
        # virus inserted a lot or added a lot
        print(max(0,len(viral) - len(clean)))
         
        sys.exit()


    if not foundStart:
        if clean[s] == viral[s]:
            start += 1
        else:
            foundStart = True
    if not foundEnd:
        if clean[e] == viral[e]:
            end += 1
        else:
            foundEnd = True
print( len(viral) - end - start)




