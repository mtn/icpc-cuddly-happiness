
#ifndef __GRAPH_H__
#define __GRAPH_H__

#include <list>
#include <string>
#include <unordered_map>

typedef std::string Key;
typedef int         Value;
typedef int         Weight;

/**
 * Implementation layer for adjacency table which should be mostly hidden.
 *
 */
class GraphNode{
  public:
    GraphNode(Value value) : value(value) {};
    ~GraphNode();

    Value value;

    const std::unordered_map<Key, Weight>* getNeighbors() const;
    void addNeighbor(const Key& k, Weight weight);
    bool containsNeighbor(const Key& k) const;
    Weight getNeighbor(const Key& k) const;
    Weight setNeighbor(const Key& k, Weight weight);
    Weight removeNeighbor(const Key& k);

    bool operator==(const GraphNode* g) const;

    void print() const;

  private:
    std::unordered_map<Key, Weight> neighbors;
};

/**
 * A class which stores nodes and edges. Allows for insertion and removal of
 * removal and edges.
 */
class Graph{

  public:
    ~Graph();

    /**
     * Input:  Key to check if a node of that id is in the graph.
     * Output: Whether or not there is a node called Key in the graph
     */
    bool containsNode(const Key& k) const;
    /**
     * Assign the value v to the key k in the graph.
     */
    void insertNode(const Key& k, Value v);
    /**
     * Change the value of key k in the graph to v. If k is not already
     * in the graph this function will assign to k but return 0
     * Output: Return the previous value stored in v.
     */
    Value updateNode(const Key& k, Value v);
    /**
     * Remove the node k from the graph and any edges connected to it
     * Input:  A key k to remove from the graph.
     * Output: The value previously stored in k before removal.
     */
    Value removeNode(const Key& k);
    /**
     * Create an edge from key k to key v with the given weight.
     * Input: 2 Keys to create an edge between and a weight to assign that edge.
     */
    void makeEdge(const Key& k, const Key& v, Weight weight);
    /**
     * Change the weight of the edge going from k to v to the given weight
     * Input:  The keys for the edge and the weight to change the edge to
     * Output: The previous weight of the edge.
     */
    Weight  updateEdge(const Key& k, const Key& v, Weight weight);
    /**
     * Remove the edge between the keys k and v.
     * Input:  The keys to remove the edge between.
     * Output: The weight of the edge removed.
     */
    Weight  removeEdge(const Key& k, const Key& v);
    /**
     * Get a the data attached to a specific node in the graph.
     * Input:  The key which references the node
     * Output: The GraphNode stored at that location. Contains the value stored
     *         as well as all of the edges.
     */
    const GraphNode* getNode(const Key& k) const;
    /**
     * Gets the value of the node stored for a certain key
     * Input:  The key to get the value of.
     * Output: The value stored in the node of the given key.
     */
    const Value operator[](const Key& k) const;

    /**
     * Create a copy of this graph.
     */
    Graph* clone();

    /**
     * Input:  KeyType (Typically String or int) which is the start node
     * Output: A Graph where each node is connected to at most one other node
     *         and there are no cycles. Traversing the graph from any point
     *         will yield the shortest path to the given start node from that
     *         node. If no connection exists from the start node to a node n,
     *         that n will not be in the graph. The value at any node in the
     *         output graph is the length of the path to the start node.
     */
    Graph* dijkstra(Key startNode);

  private:
    /**
     * Input:  A start and terminal node for path
     * Output: A graph similar dijkstra's but where instead of shortest paths
     *         the largest minimum weight is prioritized
     */
   Graph* frodFulkersonDij(const Key& source, const Key& terminal);
   public:
    /**
     * Input:  A start and terminal node
     * Output: A weight representing the max flow of a graph
     */
    Weight fordFulkerson(const Key& source, const Key& terminal);

    /**
     * Input:  Another graph to determine equality with
     * Output: Returns true if the graphs have the same edges and verticies
     */
    bool operator==(const Graph* g) const;

    /**
     * Print out the contents of the graph. Contains node names, values and edges.
     */
    void print() const;

  private:
    // The backing unordered map which stores nodes to their names.
    std::unordered_map<Key, GraphNode*> nodes;
};

#endif
