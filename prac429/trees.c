#include <stdio.h>
#include <stdlib.h>

int main(){
    int numSeeds, lastDay = 0, temp, treedays;
    scanf("%d",&numSeeds);
    int *arr = malloc(sizeof(int) * numSeeds);
    for(int i = 0; i < numSeeds; i++){

    }
    for(int i = 1; i <= numSeeds; i++){
        scanf("%d",&treedays);
        temp = i + treedays;
        if(temp > lastDay) lastDay = temp;
    }
    printf("%d",lastDay);
}
