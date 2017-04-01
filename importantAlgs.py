import heapq

def union(data,a,b):
    '''
    Input: list of integers pointing to parents (representatives of sets)
    Combines the sets contianing a, and b
    '''
    ra,rb = find(data,a),find(data,b)
    if data[ra] < data[rb]: # then |a| > |b| because negatives
        # update |a| and make b's root ra
        data[ra] += data[rb]
        data[rb] = ra
    else:
        # update |b| and make a's root rb
        data[rb] += data[ra]
        data[ra] = rb

def find(data,node):
    '''
    returns parent id and updates everyone in the path to lead to parent
    '''
    # while not a root, flow up to parent
    path = []
    while data[node] >= 0:
        node = data[node]
        path.append(node)
    # compress path
    for n in path:
        data[n] = node
    # return parent
    return node

def dykstra(graph,source):
    """
    finds the single source all destinations shortest paths on a non-negative
    weighted tree.
    Input:  Dictionary { node : {neighbor:weight} }
    Output: Dictionaries dist and prev
    """
    unVisited = set(graph.keys())
    dist = {u: float('inf') for u in graph.keys() }
    prev = {u: None for u in graph.keys() }
    # Initialize source and priority queue
    dist[source] = 0
    closestHeap = heapq.heapify( [(w,n) for n,w in graph[source] ] )

    while len(unVisited) == 0:
        node = heapq.heappop(closestHeap)
        unVisited.remove(node)
        for neighbor, weight in graph[node].items():
            assert weight >= 0, 'negative weights'
            alt = dist[node] + weight
            if alt < dist[neighbor]:
                # By induction this is the shortest path to neighbor
                dist[neighbor] = alt
                prev[neighbor] = node
                heapq.heappush(closestHeap,(alt,node))
    return dist, prev

def BellmanFord(graph,source):
    """
    Like Dykstra's but supports negative weights
    # dynamic progrmming
    Input:  Dictionary { node : {neighbor:weight} }
    Output: Dictionaries: distance, previous
    """
    dist = {}; prev = {}; edges = []
    for u in graph:
        dist[u] = float('inf')
        prev[u] = None
        edges += [(u,v,weight) for v,weight in graph[u].items()]
    dist[source] = 0
    # Relax repeatedly
    for i in range(1,len(graph)):
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
    # Check for negative weight cycles
    for u,v,w in edges:
        assert dist[u] + w >= dist[v], 'negative weight cycle'
    return dist,prev

def Kruskall(graph):
    """
    Returns minimum spanning tree of graph
    Input: Dictionary { node : {neighbor:weight} }
    """
    edges = []
    for u in graph:
        edges += [(w,u,v) for v,w in graph[u] ]
    edges.sort()
    keyMap = {node:num for num,node in enumerate(graph.keys())}
    UF = [ -1 for i in graph.keys() ]
    minSpanTree = {}
    for w,u,v in edges:
        ku,kv = keyMap(UF, u),keyMap(UF, v) # key in unionFind datastructure
        pu,pv = find(UF, ku), find(UF, kv) # parent
        if pu != pv:
            minSpanTree[u] = minSpanTree.get(u,[]) + [v]
            minSpanTree[v] = minSpanTree.get(v,[]) + [u]
            union(UF,pu,pv)
    return minSpanTree

def FordFulkerson(Graph, source, terminal):
    """
    Returns maximum flow between source and terminal nodes of a graph
    """
    print('haha')
