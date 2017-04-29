#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(){
    int num;
    scanf("%d",&num);
printf("%d\n",num);
    char* n1 = malloc(sizeof(int)*1000);
    int stopReading = 0;
    for(int i = 0; i < 1000; i++){
        int temp = getchar();
        if (temp == '\n' || temp == EOF)
            break;
        n1[i] = temp =='1';
    }
    int deleted = 1;
    for(int i = 0; i < 1000; i++){
        int temp = getchar();
        if (temp == '\n' || temp == EOF)
        {
            break;
        }
        if (n1[i] != (temp=='1') && num % 2 == 0){
            deleted = false;
            break;
        }
        if(n1[i] == (temp=='1') && num % 2 == 1){
            deleted = false;
            break;
        }

    }

    if(deleted) puts("Deletion succeeded");
    else puts("Deletion failed");
}

