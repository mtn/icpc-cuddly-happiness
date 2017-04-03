
#include <iostream>
#include <queue>
#include <set>

#include "Graph.h"

// From: http://stackoverflow.com/questions/3767869/adding-message-to-assert
#ifndef NDEBUG
#   define ASSERT(condition, message) \
    do { \
        if (! (condition)) { \
            std::cerr << "Assertion `" #condition "` failed in " << __FILE__ \
                      << " line " << __LINE__ << ": " << message << std::endl; \
            std::terminate(); \
        } \
    } while (false)
#else
#   define ASSERT(condition, message) do { } while (false)
#endif

GraphNode::~GraphNode()
{

}

const std::list<std::pair<const Key, Weight>>* GraphNode::getNeighbors() const
{
  return &this->neighbors;
}

void GraphNode::addNeighbor(const Key& k, Weight weight)
{
  this->neighbors.push_front(std::pair<Key, Weight>(k, weight));
}

void GraphNode::removeNeighbor(const Key& k)
{
  // For each neighbor, remove if the neighbor's key is k
  for (auto it = this->neighbors.begin(); it != this->neighbors.end();)
  {
    // If the key of this element of the list is the given key
    if (it->first == k)
    {
      // Remove this item from the neighbors list and get the iterator
      // to the element right after the removed one
      it = this->neighbors.erase(it);
    }
    else // Otherwise advance the iterator past this element of the list
      ++it;
  }
}

/**
 * Input:  Pointer to another graph node
 * Output: Whether or not the value stored in these two nodes
 *         are the same as well as their connections.
 */
bool GraphNode::operator==(const GraphNode* g) const
{
  if (value != g->value) return false;

  // Check to see if they have the same edges
  for (auto it = this->neighbors.begin(); it != this->neighbors.end(); ++it)
  {
    // If the element at it is not within neighbors, return false
    // They don't have the same items
    if (std::find(g->neighbors.begin(), g->neighbors.end(), *it) == g->neighbors.end())
    {
      std::cout << "no index found in first\n";
      return false;
    }
  }

  // Make sure that there are no elements in this GraphNode that are not
  // in the other
  for (auto it = g->neighbors.begin(); it != g->neighbors.end(); ++it)
  {
    // If the element at it is not within neighbors, return false
    // They don't have the same items
    if (std::find(this->neighbors.begin(), this->neighbors.end(), *it) == this->neighbors.end())
    {
      std::cout << "no index found in last\n";
      return false;
    }
  }

  return true;
}

Graph::~Graph()
{
  auto it = this->nodes.begin();
  for (;it != this->nodes.end(); ++it)
  {
    delete it->second;
  }
}

// Determine if the backing map of nodes contains key
bool Graph::containsNode(const Key& k) const
{
  return this->nodes.find(k) != this->nodes.end();
}

// Insert a new node Weighto the graph with the given value
void Graph::insertNode(const Key& key, Value value)
{
  this->nodes[key] = new GraphNode(value);
}

Value Graph::updateNode(const Key& key, Value newValue)
{
  Value prevValue = this->nodes[key]->value;
  this->nodes[key]->value = newValue;
  return prevValue;
}

Value Graph::removeNode(const Key& key)
{
  // Get the value of the removed node
  GraphNode* node = this->nodes[key];
  Value value = node->value;

  // Create an iterator and go through each element in the map and remove
  // any edges from nodes to the node named key
  for (auto it = this->nodes.begin(); it != this->nodes.end();)
  {
    // Skip the key being removed itself
    if (it->first == key)
    {
      // Remove nodes matching key from the graph.
      it = this->nodes.erase(it);
    }

    // Otherwise, remove neighbors to the attached node originating from key
    it->second->removeNeighbor(key);
    ++it;
  }

  // Get rid of the node at that position.
  delete node;

  // Return value of the removed node
  return value;
}

const GraphNode* Graph::getNode(const Key& key) const
{
  return this->nodes.find(key)->second;
}

const GraphNode* Graph::operator[](const Key& key) const
{
  return this->getNode(key);
}

// Create an edge between two new nodes of the graph
void Graph::makeEdge(const Key& k, const Key& j, Weight weight)
{
  // Ensure that both given nodes are in the graph
  if (containsNode(k))
  {
    if (containsNode(j))
      this->nodes[k]->addNeighbor(j, weight); // If both are link them together
    else
      ASSERT(0, "Graph Does Not Contain " + j);
  }
  else
    ASSERT(0, "Graph Does Not Contain " + k);
}

struct WeightPair
{
  Key k;
  Key from;
  Weight w;
};

bool operator<(const WeightPair& a, const WeightPair& b)
{
  return a.w > b.w;
}

void printWP(WeightPair wp)
{
  std::cout << "WP: " << wp.k << " (" << wp.w << ") from " << wp.from << "\n";
}

/**
 * Finds the shortest path from the start node to every node it is connected to.
 *
 * Input: A key in the graph
 * Output: A graph where each node holds the distance from the startNode to
 * that node and is connected to only one other node, the node closest to the
 * startNode from that node.
 */
Graph* Graph::dijkstra(Key startNode)
{
  if (containsNode(startNode))
  {
    Graph* outGraph = new Graph();

    std::priority_queue<WeightPair> nextNodes;
    nextNodes.push(WeightPair{startNode, startNode, 0});

    while (!nextNodes.empty())
    {
      // Dequeue the next item from the queue
      WeightPair wp = nextNodes.top();
      nextNodes.pop();

      // Determine if the node that this item is representing has already been
      // added to the graph
      if (outGraph->containsNode(wp.k))
      {
        // If so, skip this item.
        continue;
      }
      else
      {
        // If not, add it into the graph. It is the least distance node from
        // start at this point. Then enqueue all attached nodes.
        outGraph->insertNode(wp.k, wp.w);
        if (wp.k != wp.from)
          outGraph->makeEdge(wp.k, wp.from, wp.w - (*outGraph)[wp.from]->value);

        auto neighbors = (*this)[wp.k]->getNeighbors();
        for (auto it = neighbors->begin(); it != neighbors->end(); ++it)
        {
          // Push a WeightPair which points to the node at the end of this edge,
          // points from the current node we are looking at, and has a weight
          // of the distance from this node to the start plus the edge.
          nextNodes.push(WeightPair{it->first, wp.k, wp.w + it->second});
        }
      }
    }

    return outGraph;
  }
  else
    ASSERT(0, "Graph Does Not Contain " + startNode);
  return nullptr;
}

/**
 * Input:  A Graph*
 * Output: Whether or not this Graph has the same nodes and edges as the given
 */
bool Graph::operator==(const Graph* g) const
{
  std::cout << "Calling Equality\n";
  // For every element node in this graph
  auto it = this->nodes.begin();
  for (;it != this->nodes.end(); ++it)
  {
    // If the other map does not contain the same keys as this one then we
    // have failed
    if (!g->containsNode(it->first))
    {
      std::cout << "Missing node " << it->first << "\n";
      return false;
    }

    // Ensure that edges and values stored are the same
    if (!(*((*this)[it->first]) == (*g)[it->first])) return false;
  }

  // Check that the other Graph has no nodes in it that this does not.
  it = g->nodes.begin();
  for (;it != g->nodes.end(); ++it)
  {
    if (!this->containsNode(it->first)) return false;
  }

  // If the Graphs have the same nodes with the same edges return true.
  return true;
}

void GraphNode::print() const
{
  std::cout << "Value: " << value << '\n';
  for (auto it = this->neighbors.begin(); it != this->neighbors.end(); ++it)
  {
    std::cout << "Neighbor: " << it->first << " (" << it->second << ")\n";
  }
}

void Graph::print() const
{
  for (auto it = this->nodes.begin(); it != this->nodes.end(); ++it)
  {
    std::cout << "Node (" << it->first << ")";
    it->second->print();
  }
}
