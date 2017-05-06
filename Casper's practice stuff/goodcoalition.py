from functools import reduce

numTestCases = int(input())

def go():
   global opt,p,s
   numParties = int(input())
   parties = []
   for i in range(numParties):
       si, pi = [int(x) for x in input().split(' ')]
       pi = float(pi)/100
       parties.append((pi,si))
   p,s = zip(*parties) # arranged in descending order of p

   opt = [[None]*151 for p in range(numParties)]

   # DYNAMIC PROGRAMMING

   for i in range(numParties):
      for S in range(50):
         ssi = max(S-s[i], 0)

         if S <= s[i] and i > 0:
              opt[i][S] = max(opt[i-1][S],opt[i-1][0]*p[i],p[i] )

         elif i > 0: # S > s[i] 
              opt[0][S] = max(opt[i-1][S],opt[i-1][S-s[i]]*p[i])  

         else:       # i = 0 and any S
              opt[i][S] = 0 if s[0] < S else p[0] 


   print(opt[-1][50])

for i in range(numTestCases):
    go()


