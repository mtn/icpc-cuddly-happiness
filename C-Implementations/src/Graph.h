
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
    ~GraphNode();

    Value value;

    const std::list<std::pair<const Key, Weight>>* getNeighbors() const;
    void addNeighbor(const Key& k, Weight weight);
    void removeNeighbor(const Key& k);

    bool operator==(GraphNode* g) const;

    void print() const;

  private:
    std::list<std::pair<const Key, Weight>> neighbors;
};

class Graph{

  public:
    ~Graph();

    bool containsNode(const Key& k) const;
    void insertNode(const Key& k, Value v);
    Value updateNode(const Key& k, Value v);
    Value removeNode(const Key& k);
    void makeEdge(const Key& k, const Key& v, Weight weight);
    const GraphNode* getNode(const Key& k) const;
    const GraphNode* operator[](const Key& k) const;

    Graph* dijkstra(Key startNode);

    bool operator==(const Graph* g) const;

    void print() const;
    
  private:
    std::unordered_map<Key, GraphNode*> nodes;
};

#endif
