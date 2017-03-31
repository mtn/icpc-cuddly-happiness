import heapq

def union(data,a,b):
    '''
    Combines sets a,b
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
    Output: Dictionary { node : (length, [path] ) }
    """
    unVisited = set(graph.keys())
    dist = {u: float('inf') for u in graph.keys() }
    prev = {u: None for u in graph.keys() }
    ### Need to be completed lol


    dist[source] = 0
    while len(unVisited) > 0:


def BellmanFord(graph,source):
    """
    Like Dykstra's but supports negative weights
    # dynamic progrmming
    """
    print("lol")

def Kruskall(graph):
    """
    Returns minimum spanning tree of graph
    """
    print('lmao')

def Ford Fulkerson(Graph, source, terminal):
    """
    Returns maximum flow between source and terminal nodes of a graph
    """
    print('haha')
