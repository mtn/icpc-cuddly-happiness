import heapq

class FFGraph(object):

  def __init__(self):
    # Nodes is a dictionary in the format of
    #   {node: {node: (weight, [(pool, isReverseEdge)])}}
    self.nodes = dict()
    # Pools is a dictionary in the format of
    #   {pool: (forwardAmount, backwardAmount)}
    self.pools = dict()

  # Gets the weight of the edge connecting two nodes
  def __getitem__(self, keys):

    start, end = keys
    return self._edgeWeight(start, end)

  def _edgeWeight(self, start, end):

    # Grab the edge connecting these two nodes
    edge = self.nodes[start][end]

    # Grab the weight of said edge
    edgeWeight = edge[0]
    # And then restrict the weight to the minimal remaining flow in each pool
    # it is attached to
    for pool in edge[1]:
      edgeWeight = min(self.pools[pool[0]][(1 if pool[1] else 0)], edgeWeight)

    # return that minimal flow
    return edgeWeight

  def _decreaseEdgeWeight(self, start, end, amount):

    # Grab the edge connecting these two nodes
    edge = self.nodes[start][end]

    # Grab the weight of said edge
    amount = min(edge[0], amount)
    # And then restrict the weight to the minimal remaining flow in each pool
    # it is attached to
    for pool in edge[1]:
      amount = min(self.pools[pool[0]][1 if pool[1] else 0], amount)

    # Change the weight of this edge based on the amount to be removed
    self.nodes[start][end] = (edge[0] - amount, edge[1])
    # Change the weight of the pools based on the amount to be removed
    for pool in edge[1]:
      fWeight, rWeight = self.pools[pool[0]]
      fWeight -= (-amount if pool[1] else amount)
      rWeight += (-amount if pool[1] else amount)
      self.pools[pool[0]] = (fWeight, rWeight)
    # Change the weight of the reverse edge by amount
    edge = self.nodes[end][start]
    self.nodes[end][start] = (edge[0] + amount, edge[1])

  def newPool(self, poolName, value):

    self.pools[poolName] = (value, 0)

  def __setitem__(self, keys, weight):

    # If multiple arguments were passed
    if isinstance(keys, tuple):

      # Variables for holding data
      start, end = None, None
      edge, revEdge = None, None

      # If two arguments were passed then treat them as a start node and end
      # node and create an edge between them
      if len(keys) == 2:

        # Get the start and end nodes as variable
        start, end = keys
        # Create a new pool of flow to draw from for that edge
        self.pools[(start, end)] = (weight, 0)
        # Create the forward and reverse edges from the given nodes
        edge = (weight, [((start, end), False)])
        revEdge = (0, [((start, end), True)])

      # If three arguments are passed then treat them as a start node, end node
      # and finally a list of pools to pull from
      elif len(keys) == 3:

        start, end, pools = keys
        # Ensure pools is iterable if it is a single item
        try:
          iter(pools)
        except:
          pools = [pools]
        # Create the edge drawing from those pools
        edge = (weight, [(pool, False) for pool in pools])
        revEdge = (0, [(pool, True) for pool in pools])

      # If 4 arguments are passed further treat the 4th argument as whether a
      # given pool value is reversed. Assume false for any non-specified pool
      # values
      elif len(keys) == 4:

        start, end, pools, directions = keys
        # Ensure pools and directions are iterable if they are single items
        try:
          iter(pools)
        except:
          pools = [pools]
        try:
          iter(directions)
        except:
          directions = [directions]
        numDirections = len(directions)
        # Create the edge drawing from those pools with the specified directions
        edge = (weight, [(pools[i], False if i >= numDirections else directions[i]) for i in range(len(pools))])
        revEdge = (0, [(pools[i], True if i >= numDirections else not directions[i]) for i in range(len(pools))])

      # Add the edges to the graph
      if start in self.nodes:
        self.nodes[start][end] = edge
      else:
        self.nodes[start] = {end: edge}
      if end in self.nodes:
        self.nodes[end][start] = revEdge
      else:
        self.nodes[end] = {start: revEdge}

    # If only one key argument was passed
    else:

      # Create a new pool of that identifier
      self.pools[keys] = weight

  def _fdijkstra(self, source, terminal):
    unVisited = set(self.nodes.keys())
    dist = {u: float('inf') for u in self.nodes.keys() }
    prev = {u: None for u in self.nodes.keys() }
    # Initialize source and priority queue
    dist[source] = 0
    closestHeap = [(-float('inf'),source)]
    heapq.heapify( closestHeap )
    # Iterate until we've seen everything
    while len(unVisited) != 0:
        if len(closestHeap) == 0:
            return None,None
        prevWeight, node = heapq.heappop(closestHeap)
        if node not in unVisited:
            continue
        if node == terminal:
          break
        unVisited.remove(node)
        # bring neighbors closer
        for neighbor in self.nodes[node]:
            weight = self[node, neighbor]
            assert weight >= 0, 'negative weights'
            if weight <= 0: continue ## Skip edges that can't carry flow
            alt = max(-weight, prevWeight)
            dist[neighbor] = alt
            prev[neighbor] = node
            heapq.heappush(closestHeap, (alt,neighbor))
    return abs(dist[terminal]), prev

  def _decreasePath(self, path, amount):

    u = path[0]
    for v in path[1:]:
      self._decreaseEdgeWeight(u, v, amount)
      u = v

  def _findPath(self, source, terminal):

    dist, prev = self._fdijkstra(source, terminal)
    if dist == None or prev == None:
      return None, None

    path = [terminal]
    current = terminal
    while current != source:
      current = prev[current]
      path.insert(0, current)
    return dist, path

  def FordFulkerson(self, source, terminal):

    flow = 0
    newFlow, path = self._findPath(source, terminal)
    while path != None:

      self._decreasePath(path, newFlow)
      flow += newFlow
      newFlow, path = self._findPath(source, terminal)

    return flow

  def removePath(self, path, amount):

    for u, v in path:
      edge = self[u, v]
      edge -= amount
      if edge.weight <= 0:
        del self.nodes[u][v]
        if u in self.nodes[v]:
          del self.nodes[v][u]

if __name__ == "__main__":

  graph = FFGraph()
  graph['A', 'B'] = 1
  graph['A', 'C'] = 1
  graph['C', 'B'] = 1
  graph['C', 'D'] = 1
  graph['B', 'D'] = 1
  print(graph.FordFulkerson('A', 'D'))

  graph = FFGraph()
  graph['S', 'A'] = 1
  graph['S', 'B'] = 1
  graph['S', 'C'] = 1
  graph['S', 'D'] = 1
  graph['E', 'T'] = 2
  graph['F', 'T'] = 2
  graph[('E', 'F'), 'T', [('E', 'T'), ('F', 'T')]] = 1
  graph['A', 'E'] = 1
  graph['B', ('E', 'F')] = 1
  graph['C', 'F'] = 1
  graph['D', 'F'] = 1
  print(graph.FordFulkerson('S', 'T'))

  # Generate ford fulkerson graph for dots game
  graph = FFGraph()
  n = 3
  for x in range(n-1):
    for y in range(n-1):
      graph.newPool(("S", x, y), 3)
  for x in range(n):
    for y in range(n):
      graph[(x, y, "'"), "T"] = 1
      graph["S", (x, y)] = 1
      # Connect up
      if y - 1 >= 0:
        if x - 1 >= 0 and x < n - 1:
          graph[(x, y), (x, y-1, "'"), [("S", x, y-1), ("S", x-1, y-1)]] = 1
        elif x - 1 >= 0:
          graph[(x, y), (x, y-1, "'"), [("S", x - 1, y-1)]] = 1
        else:
          graph[(x, y), (x, y-1, "'"), [("S", x, y-1)]] = 1
      # Connect right
      if x + 1 < n:
        if y - 1 >= 0 and y < n - 1:
          graph[(x, y), (x+1, y, "'"), [("S", x, y), ("S", x, y-1)]] = 1
        elif y - 1 >= 0:
          graph[(x, y), (x+1, y, "'"), [("S", x, y-1)]] = 1
        else:
          graph[(x, y), (x+1, y, "'"), [("S", x, y)]] = 1
  print(graph.FordFulkerson("S", "T"), graph.pools.items())
