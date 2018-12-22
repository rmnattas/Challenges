#include <stdio.h>

int abs(int x){
    if (x >= 0) return x;
    else return -x;
}

int min(int a, int b){
    if (a <= b) return a;
    else return b;
}

int main(){
    int a, b;
    if( (scanf("%d/%d", &a,  &b)) != 2 ) return 1;
    
    //convert to celsius
    a -= (32 * b);
    a *= 5;
    b *= 9;

    //fraction in lowest terms
    if (a == 0) b = 1;
    int m = min(abs(a), abs(b));
    for (int i=m; i > 1; i--){
        if ( (a%i == 0) && (b%i == 0) ){
            a /= i;
            b /= i;
            break;
        }
    }
    
    printf("%d/%d", a, b);
    printf("\n");

    return 0;
}

