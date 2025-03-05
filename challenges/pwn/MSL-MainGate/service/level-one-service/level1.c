#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig)
{
    puts("\n[Security Breach]");
    puts(flag);
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
        puts("[ERROR] If you are running on the server, please contact the admin.");
        puts("[ERROR] If you are running locally, please make sure the flag.txt file is in the same directory as the binary.");
        exit(0);
    }

    fgets(flag, FLAGSIZE_MAX, f);
    fclose(f);

    signal(SIGSEGV, sigsegv_handler);

    // Drop privileges if running with elevated rights
//    gid_t gid = getegid();
 //   setresgid(gid, gid, gid);

    puts("Welcome to the Mad Scientist Lab - Main Gate Security");
    puts("Legend tells that if you crash the security system, the override code is revealed.");
    puts("Recite the forbidden incantation (input):");
    fflush(stdout);

    char buf1[100];
    gets(buf1);

    vuln(buf1);

    return 0;
}
