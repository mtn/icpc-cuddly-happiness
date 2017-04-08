
import heapq

def Dykstra(graph,source,target):
    """
    finds the single source all destinations shortest paths on a non-negative
    weighted tree.
    Input:  Dictionary { node : {neighbor:weight} }
    Output: Dictionaries dist and prev
    """
    minDist = -1
    # Initialize source and priority queue
    closestHeap = [(0,[source])]
    pathsToTarget = []
    # Iterate until we've seen everything
    while len(closestHeap) > 0:
        dist, path = heapq.heappop(closestHeap)
        current = path[0]
        # Add if path reaches terminal node, kill if too long
        if minDist >= 0:
          if dist > minDist:
            break
        if current == target:
          minDist = dist
          pathsToTarget.append(path)
        # Add neighbors to check their paths
        for neighbor, weight in graph[current].items():
            assert weight >= 0, 'negative weights'
            heapq.heappush(closestHeap, (dist + weight,[neighbor]+path))
    return minDist, pathsToTarget

def main():

  with open("TruckingTests.txt") as f:

    data = f.read().splitlines()
    n = int(data.pop(0))
    graph = {i+1 : {} for i in range(n)}
    itemsToPickUp = data.pop(0)
    nodeValues = {}
    # For each node, determine its value
    for i, item in enumerate(itemsToPickUp.split(' ')):
      nodeValues[i+1] = int(item)
    # For the next m items
    m = data.pop(0)
    for line in data:
      a, b, d = line.split(' ')
      a, b, d = int(a), int(b), int(d)
      graph[a][b] = d
      graph[b][a] = d
    dist, shortPaths = Dykstra(graph, 1, n)
    if dist == -1:
      print('impossible')
      return
    maxPoints = 0
    bestPath = None
    for path in shortPaths:
      picked = 0
      for node in set(path):
        picked += nodeValues[node]
      if picked > maxPoints:
        maxPoints = picked
        bestPath = path
    print( '%d %d'%(dist,maxPoints))

if __name__ == "__main__":

  main()
