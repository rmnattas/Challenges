#include <stdio.h>

struct point { int x, y; };

int main(){
    struct point p[3];
    scanf("%d %d", &p[0].x, &p[0].y);
    scanf("%d %d", &p[1].x, &p[1].y);
    scanf("%d %d", &p[2].x, &p[2].y);
    
    if (p[0].x == p[1].x){
        printf("%d ", p[2].x);
    } else if (p[0].x == p[2].x){
        printf("%d ", p[1].x);
    } else {
        printf("%d ", p[0].x);
    }

    if (p[0].y == p[1].y){
        printf("%d\n", p[2].y);
    } else if (p[0].y == p[2].y){
        printf("%d\n", p[1].y);
    } else {
        printf("%d\n", p[0].y);
    }

    return 0;
}

