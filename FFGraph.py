import heapq

class Edge(object):

  def __init__(self, weight, start, end, revEdge=None):

    self.weight = weight
    self.start = start
    self.end = end
    self.revEdge = None

  def __isub__(self, other):

    if isinstance(other, Edge):

      self.weight -= other.weight
      if self.revEdge:
        self.revEdge.weight += other.weight

    else:

      self.weight -= other
      if self.revEdge:
        self.revEdge.weight += other

    return self

  def __str__(self): return str(self.weight)
  def __repr__(self): return str(self.weight)

class RelatedEdge(object):

  def __init__(self, connectedEdges, weight, start, end, revEdge=None):

    self.connectedEdges = connectedEdges
    self._weight = weight
    self.start = start
    self.end = end
    self.revEdge = None

  @property
  def weight(self):
    # Get the minimum weight of the edges this node is fused
    # to and the weight of this node itself
    weight = self._weight
    for edge in self.connectedEdges:
      weight = min(weight, edge.weight)
    return weight

  @weight.setter
  def weight(self, newWeight):

    difference = newWeight - self._weight
    for edge in self.connectedEdges:
      edge.weight += difference
    self._weight = newWeight

  def __isub__(self, other):

    if isinstance(other, Edge):

      other = other.weight

    self.weight -= other
    if self.revEdge:
      self.revEdge.weight += other

    return self

  def __str__(self): return str(self.weight)
  def __repr__(self): return str(self.weight)

class FFGraph(object):

  def __init__(self):
    self.nodes = dict()

  def __getitem__(self, keys):

    start, end = keys
    return self.nodes[start][end]

  def __setitem__(self, keys, value):

    start, end = None, None
    if len(keys) == 2:
      start, end = keys
      newEdge = Edge(value, start, end)
      revEdge = Edge(0, end, start, newEdge)
      newEdge.revEdge = revEdge

      if start in self.nodes:
        self.nodes[start][end] = newEdge
      else:
        self.nodes[start] = {end: newEdge}
      if end in self.nodes:
        self.nodes[end][start] = revEdge
      else:
        self.nodes[end] = {start: revEdge}

  def join(self, edges, weight):

    #ensure edges go to same place, have large enough weights, etc
    end = edges[0].end
    revEdges = []
    starts = []
    for edge in edges:
      if edge.end != end: return
      if edge.weight < weight: return
      starts.append(edge.start)
      if edge.revEdge:
        revEdges.append(edge.revEdge)

    start = tuple(starts)
    newEdge = RelatedEdge(edges, weight, start, end)
    revEdge = RelatedEdge(revEdges, weight, end, start)
    newEdge.revEdge = revEdge

    if start in self.nodes:
      self.nodes[start][end] = newEdge
    else:
      self.nodes[start] = {end: newEdge}
    if end in self.nodes:
      self.nodes[end][start] = revEdge
    else:
      self.nodes[end] = {start: revEdge}

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
        for neighbor, edge in self.nodes[node].items():
            weight = edge.weight
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
      edge = self[u, v]
      edge -= amount
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
  graph.join([graph['E', 'T'], graph['F', 'T']], 1)
  graph['A', 'E'] = 1
  graph['B', ('E', 'F')] = 1
  graph['C', 'F'] = 1
  graph['D', 'F'] = 1
  print(graph.FordFulkerson('S', 'T'))
