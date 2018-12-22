#include <iostream>
#include <bitset>
#include <algorithm>
using namespace std;

int main(){
    int cases; cin >> cases;
    for (int i=0; i<cases; i++){
        int x; cin >> x;
        int result = 0;
        do {
            string binary = bitset<33>(x).to_string();
            int case_result = count(binary.begin(), binary.end(), '1');
            if (case_result > result) { result = case_result; }
            x /= 10;
        } while (x>0);

        printf("%d\n", result);

    }

    return 0;
}

