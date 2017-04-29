import sys


d = {}

d[0] = {'***':{0,2,3,5,6,7,8,9},'  *':{1},           '* *':{4}}
d[1] = {'* *':{0,4,8,9},        '  *':{1,2,3,7},     '*  ':{5,6}}
d[2] = {'***':{2,3,4,5,6,8,9},  '* *':{0},           '  *':{1,7}}
d[3] = {'* *':{0,6,8},          '  *':{1,3,4,5,7,9}, '*  ':{2}}
d[4] = {'***':{0,2,3,5,6,8,9},  '  *':{1,4,7}}

lines = []
try:
    for i in range(5):
        lines.append(input())
except:
    print('BOOM!!')
    sys.exit()

for l in lines:
    if len(l) != len(lines[0]):
       print('BOOM!!')
       sys.exit()

sets = [{0,1,2,3,4,5,6,7,8,9} for i in range(0, len(lines[0]),4)]

for i in range(5):
    for j in range(len(sets)):
        lb = j*4
        rb = lb + 3

        keyy = lines[i][lb:rb] # 3 digit keys
        if keyy in d[i]:
            sets[j] &= d[i][keyy]
        else:
            print('BOOM!!')
            sys.exit()

final = ''
for i, s in enumerate(sets):
    #  print(i)
    final += str(s.pop())

#print(final)

if int(final) %6 == 0:
    print('BEER!!')
else:
    print('BOOM!!')


