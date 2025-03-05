#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void vuln()
{
    char buffer[64];
    unsigned int secret_key = 0;

    printf("Enter the override code to unlock the secret compound: ");
    fflush(stdout);
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

        puts("\nOverride accepted!");

        fgets(flag, sizeof(flag), fp);
        flag[sizeof(flag) - 1] = '\0';
        fclose(fp);

        puts("The secret compound formula is:");
        puts(flag);
    }
    else
    {
        puts("\nAccess denied. The override key remains locked.");
    }
}

int main()
{
    ignore_me_init_buffering();
    puts("Welcome to the Mad Scientist Lab - Hidden Compound Chamber");
    puts("Deep within the lab, a secret override key protects the experimental formula.");

    vuln();

    return 0;
}
