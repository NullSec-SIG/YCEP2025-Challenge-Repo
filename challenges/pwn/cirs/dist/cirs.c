#include <stdio.h>
#include <stdlib.h>

// Compiled using gcc -o cirs -g -fno-stack-protector -Wno-stringop-overflow cirs.c

unsigned long report_number = 0;

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void file_report()
{
    char input[28];
    printf("Please input your student ID: ");
    fgets(input, 28, stdin);
    printf("Please describe the incident: ");
    fgets(input, 256, stdin);
    printf("The matter has been recorded and will be investigated. Thank you.\n");
}

void admin()
{
    // how did you even get here?
    FILE *fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open flag\n");
        exit(0);
    }
    char c;
    while ((c = fgetc(fptr)) != EOF)
    {
        printf("%c", c);
    }
    fclose(fptr);
}

int main()
{
    setup();
    srand(0xa2cdde); // random seed
    report_number = rand();
    printf("Welcome to the Cyber Incident Reporting System (CIRS)\n");
    printf("Case number: #%lu\n", &report_number);
    file_report();
    return 0;
}
