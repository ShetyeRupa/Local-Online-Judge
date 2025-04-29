#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

// Problem 1
void problem1() {
    int a, b;
    cin >> a >> b;
    cout << a + b;
}

// Problem 2
void problem2() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << max({a, b, c});
}

// Problem 3
void problem3() {
    int n;
    cin >> n;
    cout << (n % 2 ? "Odd" : "Even");
}

// Problem 4
void problem4() {
    int n, fact = 1;
    cin >> n;
    for(int i=1; i<=n; i++) fact *= i;
    cout << fact;
}

// Problem 5
void problem5() {
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    cout << s;
}

// Problem 6
void problem6() {
    int n, a=0, b=1;
    cin >> n;
    for(int i=0; i<n; i++) {
        int temp = a;
        a = b;
        b += temp;
    }
    cout << a;
}

int main(int argc, char* argv[]) {
    if(argc < 2) return 1;
    
    int problem_id = stoi(argv[1]);
    switch(problem_id) {
        case 1: problem1(); break;
        case 2: problem2(); break;
        case 3: problem3(); break;
        case 4: problem4(); break;
        case 5: problem5(); break;
        case 6: problem6(); break;
    }
    return 0;
}