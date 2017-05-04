#include <stdio.h>

int main(){
    int num, divisor, a, b;
    scanf("%d %d",&num,&divisor);
    while(!(num == 0 && divisor == 0)){
        a = num/divisor;
        b = num%divisor;
        printf("%d %d / %d\n",a,b,divisor);
        scanf("%d %d",&num,&divisor);
    }
}
