#include <iostream>
using namespace std;
int main() {
    int n, a=0, b=1;
    cin >> n;
    for(int i=0; i<n; i++) {
        int temp = a;
        a = b;
        b += temp;
    }
    cout << a;
    return 0;
}