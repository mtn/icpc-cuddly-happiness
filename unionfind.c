#include <stdlib.h>

typedef int nodeID;

// Combine two equivalence classes
// Takes an index, returns the id of its root
nodeID find(nodeID* ns, nodeID n){
    nodeID copy = n;
    while(ns[n] >= 0)
        n = ns[n];
    // Compress path
    while(ns[copy] >= 0){
        ns[copy] = n;
        copy = ns[copy];
    }
    return n;
}

void union_sets(nodeID* ns, nodeID n1, nodeID n2){
    nodeID n1Root = find(ns,n1);
    nodeID n2Root = find(ns,n2);

}


void up_trees_new(nodeID* parentID, int size) {
    for(int i = 0; i < size; ++i)
        parentID[i] = -1;
}

