import sys


line1 = '***|  *|***|***|* *|***|***|***|***|***'
line2 = '* *|  *|  *|  *|* *|*  |*  |  *|* *|* *'
line3 = '* *|  *|***|***|***|***|***|  *|***|***'
line4 = '* *|  *|*  |  *|  *|  *|* *|  *|* *|  *'
line5 = '***|  *|***|***|  *|***|***|  *|***|***'

def todict(line):
   d = {}
   for num,ascii in enumerate(line.split('|')):
       d[ascii] = d.get(ascii,set()) | {num}
   return d

d = [ None ] * 5
for i, line in enumerate([line1,line2,line3,line4,line5]):
    d[i] = todict(line)

x = [ input() + ' '  for i in range(5) ] 

numDigits = len(x[0]) / 4
if numDigits.is_integer():
    numDigits = int(numDigits)
else:
    print('BOOM! one')
    sys.exit()

poss = [ set(range(10)) for _ in range(numDigits) ] 

for lineNo, code in enumerate(x):
    for c, place in enumerate(range(0,numDigits*4,4)):
        ascii = x[lineNo][place:place+3]
        poss[c] &= d[lineNo].get(ascii,set())

final = ''
for s in poss:
    if len(s) != 1:
       print('BOOM!!')
       sys.exit()
    num = s.pop()
    final = final + str(num)

if int(final) % 6==0:
    print('BEER!!')
else:
    print('BOOM!!')










