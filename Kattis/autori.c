#include <stdio.h>

int main(){
    char line[100] = { 0 };
    scanf("%s", line);

    printf("%c", line[0]);
    for (int i=1; i<100; i++){
        if(line[i] == '-'){
            printf("%c", line[i+1]);
            i++;
        } else if (line[i] == 0){
            break;
        }
    }
    printf("\n");

    return 0;
}

