// gcc chal.c -no-pie -o chal
#include <stdio.h>
#include <stdlib.h>
void dump(unsigned char* addr){
    for(int i=0;i<32;i++){
        if(i%16 == 0)
            printf("\nhackme + 0x%02x - ", i);
        printf("%02x ", addr[i]);
    }
    printf("\n%39s%s\n", "", "|_______________________| - changeme");
}
int said = 0;
int main(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    char hackme[24] = {0};
    unsigned long long changeme = 0;
    printf("Welcome to pwn 100! In this challenge, you will need to set changeme to 0x6942694269426942.\n");
    printf("STACK DUMP");
    dump(hackme);
    printf("changeme = 0x%016llx\n", changeme);
    printf("In order to beat this challenge, you will need to overflow into changeme and set its value.\nGood luck!\n\n");
    while(1){
        printf("Please enter data you wish to insert into hackme: ");
        gets(hackme);
        printf("\nSTACK DUMP");
        dump(hackme);
        printf("changeme = 0x%016llx\n", changeme);
        if(changeme == 0x6942694269426942){
            printf("Congratulations! Here is your flag: YCEP25{st4cksm4sh1ng}\n");
            exit(0);
        }else if(changeme == 0x4269426942694269 && said != 2){
            said = 2;
            printf("You are almost there! Remember, this challenge is running on amd64, which is a Little Endian architecture\n");
        }else if(changeme != 0 && !said){
            said = 1;
            printf("Congratulations! You have managed to override changeme. Now, do that but set its value to 0x6942694269426942\n");
        }
    }
}