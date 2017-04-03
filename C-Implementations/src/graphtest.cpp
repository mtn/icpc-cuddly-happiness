
#include <iostream>
#include "Graph.h"

int main(void)
{
  // Create a graph
  Graph input;

  // Insert 7 nodes
  input.insertNode("A", 1);
  input.insertNode("B", 2);
  input.insertNode("C", 3);
  input.insertNode("D", 4);
  input.insertNode("E", 5);
  input.insertNode("F", 6);
  input.insertNode("G", 7);
  input.insertNode("H", 8);
  // Create edges between nodes
  input.makeEdge("A", "B", 5);
  input.makeEdge("A", "C", 7);
  input.makeEdge("B", "C", 1);
  input.makeEdge("B", "F", 5);
  input.makeEdge("C", "A", 7);
  input.makeEdge("C", "B", 7);
  input.makeEdge("C", "F", 3);
  input.makeEdge("C", "D", 9);
  input.makeEdge("D", "E", 2);
  input.makeEdge("D", "G", 5);
  input.makeEdge("E", "A", 3);
  input.makeEdge("F", "G", 15);
  input.makeEdge("G", "C", 8);
  input.makeEdge("G", "F", 2);
  input.makeEdge("G", "H", 1);

  // Create the dijkstra uptree centered at "A"
  Graph* output = input.dijkstra("A");

  // Create the expected output graph
  Graph expectedOutput;
  expectedOutput.insertNode("A", 0);
  expectedOutput.insertNode("B", 5);
  expectedOutput.insertNode("C", 6);
  expectedOutput.insertNode("D", 15);
  expectedOutput.insertNode("E", 17);
  expectedOutput.insertNode("F", 9);
  expectedOutput.insertNode("G", 20);
  expectedOutput.insertNode("H", 21);
  // Add in the expected path edges
  expectedOutput.makeEdge("B", "A", 5);
  expectedOutput.makeEdge("C", "B", 1);
  expectedOutput.makeEdge("D", "C", 9);
  expectedOutput.makeEdge("E", "D", 2);
  expectedOutput.makeEdge("F", "C", 3);
  expectedOutput.makeEdge("G", "D", 5);
  expectedOutput.makeEdge("H", "G", 1);

  bool gotExpected = (expectedOutput == output);
  std::cout << "Got expected output:" << gotExpected << '\n';
  if (!gotExpected)
  {
    std::cout << "Output Graph\n";
    output->print();
    std::cout << "Expected Output Graph:\n";
    expectedOutput.print();
  }

  Graph ff0;
  ff0.insertNode("s", 0);
  ff0.insertNode("a", 1);
  ff0.insertNode("b", 2);
  ff0.insertNode("t", 3);
  // Make edges
  ff0.makeEdge("s", "a", 1);
  ff0.makeEdge("a", "t", 1);
  ff0.makeEdge("s", "b", 1);
  ff0.makeEdge("b", "a", 1);
  ff0.makeEdge("b", "t", 1);

  std::cout << "Ford Fulkerson Result: " << ff0.fordFulkerson("s", "t") << "\n";
}
