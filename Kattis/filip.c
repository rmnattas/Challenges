#include <stdio.h>


int flip(int x){
    int result = 0;
    result += (x%10)*100;
    x /= 10;
    result += (x%10)*10;
    x /= 10;
    result += x%10;

    return result;
}


int main(){
    int n1, n2;
    scanf("%d %d", &n1, &n2);

    int rn1 = flip(n1);
    int rn2 = flip(n2);

    if (rn1 > rn2){ printf("%d\n", rn1); }
    else { printf("%d\n", rn2); }


    return 0;
}

