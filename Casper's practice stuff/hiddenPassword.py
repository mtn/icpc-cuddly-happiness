
a, S = input().split(' ')

place = 0
forbidden = set(a[1:])
for s in S:
    if s == a[place]:
        place += 1
        forbidden = set(a[place+1:])
        if place == len(a):
            break
    elif s in forbidden:
        place = -1
        break

if place == len(a):
    print('PASS')
else:
    print('FAIL')
