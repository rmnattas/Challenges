#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n; cin >> n;
    int result = 0;
    for (int i=0; i<n; i++){
        int x; cin >> x;
        int power = x%10;
        x /= 10;
        result += pow(x, power);
    }
    
    printf("%d\n", result);

    return 0;
}

