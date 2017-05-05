import sys


rects = []
for i in range(3):
    r = sorted([int(x) for x in input().split(' ')])[::-1]  
    rects.append(r)
rects.sort()
rects = rects[::-1]

l,m,s = rects

if m[0] == l[0]:
    if s[0] == m[0] and l[0] == l[1] + m[1] + s[1]:
        print('YES')
    else:
        print('NO')
else:
    l0 = l[0]
    r = l[0] - l[1]
    if   l0 == m[0] + s[0] and r == m[1] + s[1]:
        print('YES')
    elif l0 == m[1] + s[0] and r == m[0] + s[1]:
        print('YES')
    elif l0 == m[0] + s[1] and r == m[1] + s[0]:
        print('YES')
    elif l0 == m[1] + s[1] and r == m[0] + s[0]:
        print('YES')
    else:
        print('NO2')




