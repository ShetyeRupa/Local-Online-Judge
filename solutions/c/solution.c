#include <stdio.h>
#include <string.h>

// Problem 1: Sum of Two Numbers
void problem1() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", a + b);
}

// Problem 2: Maximum of Three Numbers
void problem2() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d", (a > b) ? (a > c ? a : c) : (b > c ? b : c));
}

// Problem 3: Even or Odd
void problem3() {
    int n;
    scanf("%d", &n);
    printf(n % 2 ? "Odd" : "Even");
}

// Problem 4: Factorial
void problem4() {
    int n, fact = 1;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) fact *= i;
    printf("%d", fact);
}

// Problem 5: String Reversal
void problem5() {
    char s[100];
    scanf("%s", s);
    for(int i=strlen(s)-1; i>=0; i--) putchar(s[i]);
}

// Problem 6: Nth Fibonacci
void problem6() {
    int n, a=0, b=1, temp;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        temp = a;
        a = b;
        b += temp;
    }
    printf("%d", a);
}

int main(int argc, char *argv[]) {
    if(argc < 2) return 1;
    
    int problem_id = atoi(argv[1]);
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