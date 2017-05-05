import itertools as itt

nRoutines = int(input())
routines = [input() for i in range(nRoutines)]

pairwiseCost = [ [0] * nRoutines for i in range(nRoutines) ]
for a in range(nRoutines):
    for b in range(a):
        pairwiseCost[a][b] = \
        pairwiseCost[b][a] = sum( (s in routines[b]) for s in routines[a] )

best = 10**100
for p in itt.permutations(range(nRoutines)):
    cost = sum( pairwiseCost[p[i]][p[i-1]] for i in range(1,nRoutines))
    best = min(best,cost)

print(best)

