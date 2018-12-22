#include <iostream>
using namespace std;

int main(){
    string word; cin >> word;
    for (int i=0; i<int(word.length()-1); i++){
        if ((word.at(i) == 's') && (word.at(i+1) == 's')){
            printf("hiss\n");
            return 0;
        }
    }
    printf("no hiss\n");

    return 0;
}

