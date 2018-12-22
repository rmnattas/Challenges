#include <stdio.h>
#include <string.h>


int main(){
    int max;
    if (!scanf("%d", &max)) return 1;

    char line[101];
    if (!scanf("%s", line)) return 1;

    char *first = line;
    int m=0, w=0;
    while(1){
        if( (m-w) == 0 ){
            if (*first == 'M'){
                m++; first++;
            }else{
                w++; first++;
            }
        }else if ( (m-w) > 0 ){
            // there is more men
            if ( (*first == 'M') && (*(first+1) == 'M') ){
                m++; first++;
            }else{
                if ( *first == 'W' ){
                    w++; first++;
                } else if (*(first+1) == 'W'){
                    w++; first++;
                    *first = 'M';
                }
                else break;
            }
        }else if ( (m-w) < 0 ){
            // there is more women
            if ( (*first == 'W') && (*(first+1) == 'W') ){
                w++; first++;
            }else{
                if ( *first == 'M' ){
                    m++; first++;
                } else if (*(first+1) == 'M'){
                    m++; first++;
                    *first = 'W';
                }
                else break;
            }
        }


        if ( ((m-w) > max) || ((w-m) > max) ) {
            printf("%d", m+w-1);
            return 0;
        }
        if ((*first) == '\0'){
            printf("%d", m+w);
            return 0;
        }
    }
    if ( ((m-w) > max) || ((w-m) > max) ) {
        printf("%d", m+w-1);
        return 0;
    }
    printf("%d", m+w);


    return 0;
}

