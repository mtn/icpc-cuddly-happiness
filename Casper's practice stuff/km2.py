import sys
import heapq

args = [int(i) for i in input().split(' ')]
numFlasks = args[0]
caps = sorted(args[1:-1])[::-1]
goal = args[-1]

root = tuple( [caps[0]] + [0]*(numFlasks - 1) )
visited = set(root)

def update_neighbors(queue,tree, place):

    for i,ci in enumerate(place):
        for j, cj in enumerate(place):
            
            if i != j and ci > 0:
                nextplace = list(place)

                leftover = ci + cj - caps[j]
                if leftover >= 0:
                    nextplace[i] = leftover
                    nextplace[j] = caps[j]
                    poured       = caps[j] - cj
                else:
                    nextplace[i] = 0
                    nextplace[j] = ci + cj
                    poured       = ci 

                nextplace = tuple( nextplace )

                if tree.get(nextplace,10**100) < tree[place] + poured:
                    heapq.heappush(queue, nextplace)

queue = []
tree = {root: 0}
update_neighbors(queue, tree, root)
tree = {root: 0}

while len(queue) > 0:
    pour, place, nextplace = heapq.heappop(queue)
    
    assert tree[place] + pour < tree.get(nextplace,float('inf'))

    if nextplace not in visited:
        visited.add(nextplace)
        print('{} -> {} : {}'.format(place,nextplace,pour))
        tree[nextplace] = tree[place] + pour

        if nextplace[0] == goal:
            print(tree[nextplace])
            sys.exit()

        queue = update_neighbors(queue, tree, nextplace)    

print('impossible')




