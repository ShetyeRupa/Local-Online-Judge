#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    printf(n % 2 ? "Odd" : "Even");
    return 0;
}