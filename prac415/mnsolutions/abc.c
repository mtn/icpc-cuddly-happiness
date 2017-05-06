#include <stdio.h>
#include <stdlib.h>

int main(){
    int *arr = malloc(sizeof(int) * 3);
    char* str = malloc(sizeof(char)*100);
    scanf("%d %d %d",&arr[0],&arr[1],&arr[2]);
    scanf("%s",str);

    for(int i = 0; i < 3; i++)
        str[i] -= 'A';

    int max, mid, min;
    min = mid = max = 0;
    for(int i = 0; i < 3; i++){
        if(str[i] > max){
            if(max > 0) mid = max;
            max = str[i];
        }
        if(str[i] < min){
            if(min > 0) mid = min;
            min = str[i];
        }
    }

    printf("%d %d %d",min,mid,max);
}


