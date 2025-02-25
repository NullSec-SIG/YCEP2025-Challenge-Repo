#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig)
{
    printf("\n[Security Breach] %s\n", flag);
    fflush(stdout);
    exit(1);
}

void vuln(char *input)
{
    char buf2[16];
    strcpy(buf2, input);
}

int main(int argc, char **argv)
{
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
        printf("[ERROR]If you are running on the server, please contact the admin. \n");
        printf("[ERROR] If you are running locally, please make sure the flag.txt file is in the same directory as the binary.\n");
        exit(0);
    }

    fgets(flag, FLAGSIZE_MAX, f);
    signal(SIGSEGV, sigsegv_handler);

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    printf("Welcome to the Mad Scientist Lab - Main Gate Security\n");
    printf("Legend tells that if you crash the security system, the override code is revealed.\n");
    printf("Recite the forbidden incantation (input): \n\n");

    char buf1[100];
    gets(buf1);

    vuln(buf1);

    printf(".\n");
    return 0;
}
