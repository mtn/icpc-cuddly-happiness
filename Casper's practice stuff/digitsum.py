
dsum = lambda n: int(n*(n+1)/2)

def dsum(n):
   if n == 0: return 0
   if n >0  : return int(n*(n+1)/2)


nlines = int(input())

for i in range(nlines):
   a,b = input().split(' ')
   a = int(a)
   b = int(b)
   print(dsum(b) - dsum(a))

