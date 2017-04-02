
CC = /usr/bin/gcc
CFlags = -Wall -Wextra -std=c++11 -libc++

Graph = ../src/Graph.cpp ../src/Graph.h
GraphSrc = ../src/Graph.cpp

GraphTest: $(Graph) ../src/graphtest.cpp
	$(CC) $(CFlags) -o graphTest ../src/graphtest.cpp $(GraphSrc)

RunGraphTest:
	./graphTest
