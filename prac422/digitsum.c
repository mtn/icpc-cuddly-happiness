#include <stdio.h>

int main(){
    int numInp,a,b,temp;
    long long sum;
    scanf("%d",&numInp);
    for(int i = 0; i < numInp; i++){
        sum = 0;
        scanf("%d %d",&a,&b);
        while(a <= b){
            temp = a;
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            a++;
        }
        printf("%lld\n",sum);
    }
}
