#include <stdio.h>
int main() {
    int n, a=0, b=1, temp;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        temp = a;
        a = b;
        b += temp;
    }
    printf("%d", a);
    return 0;
}