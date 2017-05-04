numTrees = int(input())

arr = []
line = input()
trees = [int(i) for i in  line.split(' ')]
treesSorted = sorted(trees, reverse=True)

longest = 0
for i, t in enumerate(treesSorted):
    i += 1
    temp = t + i
    if temp > longest:
        longest = temp

print(longest+1)

