import heapq
import math

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


def residualGraph(graph, flow, delta):
    """
    Input: graph  {node : [(neighbor,capacity)]}
           flow   {(u,v) : flow}
    Delta scaling rule, residual graph ignores weights smaller than delta
    Output: residual graph {node : [(neighbor,capacity)]}
    """
    rg = {}
    for u in graph:
        for v,c in graph[u]:
            forward = flow[(u,v)]
            backward = c - flow[(u,v)]
            assert foward >= 0, 'flow error1'
            assert backward >= 0 'flow error2'
            if forward > delta:
                rg[(u,v)] = forward
            if backward > delta:
                rg[(v,u)] = backward
    return rg

def imrpovingFlow(residualGraph, source, terminal):
    """
    I: residual graph, source node, terminal node
    O: improvingFlow
    """
    dist, prev = dykstra(residualGraph,source)
    if dist[terminal] == float('inf'):
        return None
    else:
        v = terminal
        u = None
        path = []
        mincap = float('inf')
        while u != source:
            u = prev[v]
            ###

def FordFulkerson(graph, source, terminal):
    """
    I: graph { node: [(neighbor,capacity)]}
       source and terminal nodes
    O: maximum flow between source and terminal nodes of a graph
    """
    # Initialize all zero flow, and use delta scaling rule
    flow = {}
    totalCapacity = 0
    for u in graph:
        for v,cap in graph[u]:
            flow[(u,v)] = 0
            totalCapacity += cap
    delta = int(math.log2(totalCapacity))
    # Iterate until no improving flow
    while delta > 0:
    rg = residualGraph(graph,flow)
    imp_f = improvingFlow(rg,source,terminal)
    if imp_f:
        pass # Augment flow
    else:
        delta //= 2
    return flow
