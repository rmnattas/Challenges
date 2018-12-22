#include <stdio.h>

int main(){
    int x, n;
    scanf("%d", &x);
    scanf("%d", &n);

    int result = x;
    for (int i=0; i<n; i++){
        int u;
        scanf("%d", &u);
        result -= u;
        result += x;
    }
    printf("%d\n", result);

    return 0;
}

