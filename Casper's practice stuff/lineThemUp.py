
n = int(input())

lines = []
for i in range(n):
    lines.append(input())

neither = False
asc = (lines[0] < lines[1])
for i in range(1,n-1):
    if asc and lines[i] < lines[i+1]:
        continue
    elif not asc and lines[i] > lines[i+1]:
        continue
    else:
        neither = True
        break

if neither:
    print('NEITHER')
elif asc:
    print('INCREASING')
else:
    print('DECREASING')



