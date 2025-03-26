#include <stdio.h>
#include <stdbool.h>
#include <string.h>
bool isAccepted(const char *input) {
    int state = 0; 
    
    for (int i = 0; input[i] != '\0'; i++) {
        char c = input[i];
        
        if (state == 0) {
            if (c == 'a') state = 1;
            else return false;
        }
        else if (state == 1) {
            if (c == 'a') state = 1;
            else if (c == 'b') state = 2;
            else return false;
        }
        else if (state == 2) {
            if (c == 'b') state = 2;
            else return false;
        }
    }
    return state == 2;
}
int main() {
    char input[100]; 
    printf("Enter a string (only 'a' and 'b' characters): ");
    scanf("%s", input);    
    if (isAccepted(input)) {
        printf("String is ACCEPTED\n");
    } else {
        printf("String is REJECTED\n");
    }   
    return 0;
}