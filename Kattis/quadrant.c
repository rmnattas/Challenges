#include <stdio.h>

int main(){
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);

    if (x>0 && y>0){ printf("1\n"); }
    else if (x<0 && y>0){ printf("2\n"); }
    else if (x<0 && y<0){ printf("3\n"); }
    else if (x>0 && y<0){ printf("4\n"); }

    return 0;
}

