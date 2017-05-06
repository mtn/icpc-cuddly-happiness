import sys
import itertools as itt
rects = []

for i in range(3):
    r = [int(x) for x in input().split(' ')]
    rects.append(r)

def pr(a,b):
   s = '*'* a + '\n'
   s *= b
   print(s)


for a,b,c in itt.permutations(rects):
   for fa,fb,fc in itt.product([True,False],repeat=3):
      if fa: a = a[::-1]
      if fb: b = b[::-1]
      if fc: c = c[::-1]

      if a[0] == b[0] and a[0] == c[0] and a[0] == a[1] + b[1] + c[1]:
          print('YES')
          sys.exit()

      if a[0] == b[0] + c[0] and a[1] + b[1]== a[0] and a[1] + c[1] == a[0]:
          print('YES')
          sys.exit()

print('NO')
