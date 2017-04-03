
CC = clang++
CFlags = -Wall -Wextra -std=c++14 -stdlib=libc++

Graph = ../src/Graph.cpp ../src/Graph.h
GraphSrc = ../src/Graph.cpp

GraphTest: $(Graph) ../src/graphtest.cpp
	$(CC) $(CFlags) -o graphTest ../src/graphtest.cpp $(GraphSrc)

RunGraphTest:
	./graphTest
