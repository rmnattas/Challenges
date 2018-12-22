
#include <stdio.h>

int main(){

    #define F(x,y) \
    x & y | ~x & y | x & ~y | ~x & ~y

    char x=0, y=0;
    char r = F(x,y);

    printf("%d\n", r);

    if (r == -1) r = '1';
    else if (r == 0) r = '0';

    printf("%c\n", r);

    return 0;
}

