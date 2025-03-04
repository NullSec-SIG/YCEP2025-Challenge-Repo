#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function you need to call
void call_me() {
    printf("Congrats! You called call_me!\n");
    printf("YCEP25{REDACTED}");
}

// Vulnerable function
void vulnerable() {
    char buffer[71]; // Small buffer

    printf("Enter your input: ");
    gets(buffer); // Unsafe function: Buffer Overflow vulnerability
    printf("You entered: %s\n", buffer);
}

int main() {
    setbuf(stdout, NULL);
    vulnerable(); // Call the vulnerable function
    return 0;
}
