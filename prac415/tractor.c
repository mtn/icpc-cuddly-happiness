#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int **memotable;
unsigned int width;
unsigned int height;

int memofunction(unsigned int x, unsigned int y, unsigned int n)
{
    if (x < 0 || y < 0 || x >= width || y >= height) return 0;
    if (memotable[x][y]) return 0;
    memotable[x][y] = 1+memofunction(x+(1 << (n-1)), y, n+1)+memofunction(x, y+(1<<(n-1)), n+1);
    return memotable[x][y];
}
int main(){
    int numTrials;
    scanf("%d",&numTrials);
    for(int i = 0; i < numTrials; i++){
        scanf("%d %d",&width,&height);
        width++;
        height++;
        memotable = malloc(width*sizeof(int*));
        for(int k = 0; k < width; k++){
            memotable[k] = malloc(height*sizeof(int));
        }
        for(int k = 0; k < width; k++)
            for(int j = 0; j < height; j++)
                    memotable[k][j] = 0;

        printf("%d\n",memofunction(0,0,1));
    }
}
