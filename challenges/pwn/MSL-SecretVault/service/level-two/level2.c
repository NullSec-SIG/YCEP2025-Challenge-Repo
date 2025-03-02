#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln()
{
    char buffer[64];
    unsigned int secret_key = 0;
    
    printf("Enter the override code to unlock the secret compound: ");
    gets(buffer);

    if (secret_key == 0x1337)
    {
        FILE *fp;
        char flag[256];

        fp = fopen("flag.txt", "r");
        if (fp == NULL)
        {
            perror("Error opening flag file");
            exit(1);
        }


        printf("\nOverride accepted!\n");
        printf("The secret compound formula is: %s\n", flag);
    }
    else
    {
        printf("\nAccess denied. The override key remains locked.\n");
    }
}

int main()
{
    setbuf(stdout, NULL);
    printf("Welcome to the Mad Scientist Lab - Hidden Compound Chamber\n");
    printf("Deep within the lab, a secret override key protects the experimental formula.\n");

    vuln();

    return 0;
}
