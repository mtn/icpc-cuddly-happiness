import sys
import heapq

l = [int(i) for i in input().split(' ')]
n = l[0]
caps = sorted(l[1:-1])[::-1]
goal = l[-1]

root = [caps[0]] + [0] * (n - 1)
root = tuple(root)

def addNeighbors(queue, dist, place):
    
    for i, ci in enumerate(place):
        for j, cj in enumerate(place):
            if i != j and ci > 0:
                # pour from i to j
                if ci + cj <= caps[j]:
                    poured = ci
                else:
                    poured = caps[j] - cj
                
                nextplace = list(place)
                nextplace[i] -= poured
                nextplace[j] += poured
                nextplace = tuple(nextplace)

                if dist[place] + poured < dist.get(nextplace,10**1000):
                    dist[nextplace] = dist[place] + poured
                    heapq.heappush(queue, (dist[nextplace], nextplace) )
    return queue, dist

dist = {root: 0}

queue = []
processed = set([root])
queue, dist = addNeighbors(queue,dist,root)

while len(queue) > 0:
    _, node = heapq.heappop(queue)
    if node[0] == goal:
        print( dist[node])
        sys.exit()
    if node not in processed:
        processed.add(node)
        queue, dist = addNeighbors(queue,dist,node)
        
print('impossible')

