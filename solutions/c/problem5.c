#include <stdio.h>
#include <string.h>
int main() {
    char s[100];
    scanf("%s", s);
    for(int i=strlen(s)-1; i>=0; i--) putchar(s[i]);
    return 0;
}