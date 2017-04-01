
#include <iostream>
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

std::list<std::pair<const Key, Weight>> GraphNode::getNeighbors()
{
  return this->neighbors;
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

// Determine if the backing map of nodes contains key
bool Graph::containsNode(const Key& k)
{
  return this->nodes.find(k) != this->nodes.end();
}

// Insert a new node Weighto the graph with the given value
void Graph::insertNode(const Key& key, Value value)
{
  this->nodes[key] = GraphNode(value);
}

Value Graph::updateNode(const Key& key, Value newValue)
{
  Value prevValue = this->nodes[key].value;
  this->nodes[key].value = newValue;
  return prevValue;
}

Value Graph::removeNode(const Key& key)
{
  // Get the value of the removed node
  Value value = this->nodes[key].value;

  // Create an iterator and go through each element in the map and remove
  // any edges from nodes to the node named key
  for (auto it = this->nodes.begin(); it != this->nodes.end(); ++it)
  {
    // Skip the key being removed itself
    if (it->first == key) continue;

    // Otherwise, remove neighbors to the attached node originating from key
    it->second.removeNeighbor(key);
  }

  // Return value of the removed node
  return value;
}

GraphNode Graph::getNode(const Key& key)
{
  return this->nodes[key].value;
}

GraphNode Graph::operator[](const Key& key)
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
      this->nodes[k].addNeighbor(j, weight); // If both are link them together
    else
      ASSERT(0, "Graph Does Not Contain " + j);
  }
  else
    ASSERT(0, "Graph Does Not Contain " + k);
}
