
#ifndef __GRAPH_H__
#define __GRAPH_H__

#include <list>
#include <string>
#include <unordered_map>

typedef std::string Key;
typedef int         Value;
typedef int         Weight;

class GraphNode{
  public:
    GraphNode(Value value) : value(value) {};

    Value value;

    std::list<std::pair<const Key, Weight>>* getNeighbors();
    void addNeighbor(const Key& k, Weight weight);
    void removeNeighbor(const Key& k);

  private:
    std::list<std::pair<const Key, Weight>> neighbors;
};

class Graph{

  public:
    ~Graph();

    bool containsNode(const Key& k);
    void insertNode(const Key& k, Value v);
    Value updateNode(const Key& k, Value v);
    Value removeNode(const Key& k);
    void makeEdge(const Key& k, const Key& v, Weight weight);
    GraphNode getNode(const Key& k);
    GraphNode operator[](const Key& k);

    Graph* dijkstra(Key startNode);
  private:
    std::unordered_map<Key, GraphNode> nodes;
};

#endif
