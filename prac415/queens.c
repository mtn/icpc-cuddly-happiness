#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isValidIndividual(int x, int y, int** board){
    /* printf("%d %d \n",x,y); */
    for(int offset = -7; offset < 8; offset++){
        if(offset >= 0){
            if(board[x][offset] && offset != y) return false;
            if(board[offset][y] && offset != x) return false;
        }
        if(offset != 0 && x + offset >= 0 && y + offset >= 0 && x + offset < 8 && y + offset < 8){
            if(board[x+offset][y+offset]) return false;
        }
        if(offset != 0 && x - offset >= 0 && y + offset >= 0 && x - offset < 8 && y + offset < 8){
            if(board[x-offset][y+offset]) return false;
        }
    }
    return true;
}

int main(){
    int** board = malloc(8*sizeof(int*));
    for(int i = 0; i < 8; i++){
        board[i] = malloc(8*sizeof(int));
    }
    char* str = malloc(sizeof(char)*100);
    int cols[8] = {0};
    for(int i = 0; i < 8; i++){
        scanf("%s",str);
        for(int j = 0; j < 8; j++){
            if(str[j] == '.') board[i][j] = 0;
            else{
                board[i][j] = 1;
                cols[i] = j+1;
            }
        }
    }

    bool isValid = true;

    for(int i = 0; i < 8; i++)
        if(cols[i] < 1) isValid = false;

    for(int i = 0; i < 8 && isValid; i++){
        isValid = isValidIndividual(i,cols[i]-1,board);
    }

    isValid ? printf("valid") : printf("invalid");




    /* for(int i = 0; i < 8; i++){ */
    /*     for(int j = 0; j < 8; j++){ */
    /*         printf("%d ",board[i][j]); */
    /*         if(j == 7) printf("\n"); */
    /*     } */
    /* } */
}
