import sys
import heapq

line = input()
caps = [int(i) for i in line.split(' ')]

goal = caps[-1]
caps = sorted(caps[1:-1])[::-1] # n c1 ... cn V

print(caps)
print('')

root = [ caps[0] ] + [0] * (len(caps)-1)
root = tuple( root )

tree = {root:0}

if root[0] == goal:
    print( 0)
    sys.exit()

queue = [(0,root)]
heapq.heapify(queue)

while queue != []:
    _,place = heapq.heappop(queue)
    print(place)
    nextpours = []
    for i,ci in enumerate(place):
        for j,cj in enumerate(place):
            if i != j and ci > 0:
                # pour i into j
                nextplace = list(place)
                leftover = ci + cj - caps[j]
                if leftover <= 0:             # emptied container i
                    nextplace[i] = 0
                    nextplace[j] = cj + ci
                    poured = ci        
                else:                         # container j filled fully
                    nextplace[i] = leftover
                    nextplace[j] = caps[j]
                    poured = caps[j] - cj
                nextplace = tuple( nextplace )
                nextpours.append((poured,nextplace))

    nextpours.sort()
    for pour, nextplace in nextpours:
        if nextplace in tree:
            if tree[nextplace] > tree[place] + pour:
                queue = [x for x in queue if x[1] != nextplace]
                heapq.heapify(queue)
            else:
                continue

        tree[nextplace] = tree[place] + pour
        heapq.heappush(queue, (tree[nextplace], nextplace))
        if nextplace[0] == goal:
            print('\n' + str(nextplace))
            print(tree[nextplace])
            sys.exit()

print('impossible')
