#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int wallet = 69;


void ignore_me_init_buffering() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void buffer_flush(FILE *in) {
  int ch;

  do
    ch = fgetc(in);
  while (ch != EOF && ch != '\n');

  clearerr(in);
}

int main() {
  ignore_me_init_buffering();
  while (1) {
    printf(
        "Welcome to YBN's Flag Shop! Unfortunately due to global inflation "
        "and other political matters that affect financial stuff and whatnot, "
        "we have increased our prices by 100%%.\n"
        "Luckily, we have a 50%% off sale! Happy shopping!\n");

    printf("you have $%d dollars\n", wallet);
    puts("-------------------Listing-------------------");
    puts("| YBN's official fake flag - $50      (1)   |");
    puts("| YBN's official real flag - $100000  (2)   |");
    puts("| YBN hat (opening gift) - $0         (3)   |");
    puts("---------------------------------------------");

    puts("[1] Buy an item!");
    puts("[2] Help Menu");
    char input[2];
    fgets(input, 2, stdin);
    int option = atoi(input);
    if (option == 1) {
      puts("----shop----");
      printf("select the chosen item's number from the listing\n");
      fflush(stdout);
      buffer_flush(stdin);
      char item[2];
      fgets(item, 2, stdin);
      int option = atoi(item);
      if (option == 1) {
        puts("how many of the item do you want?");
        fflush(stdout);
        buffer_flush(stdin);
        char input[6];
        fgets(input, 6, stdin);
        int number = atoi(input);
        if (!(number * 50 <= wallet)) {
          puts("you do not have enough money to buy this item!");
          exit(0);
        } else {
          wallet = wallet - (number * 50);
          puts("you have received a fake flag");
          printf("Money left in wallet: $%d\n", wallet);
          puts("YBN{f4k3_fl4g}");
        }
      } else if (option == 2) {
        puts("how many of the item do you want?");
        fflush(stdout);
        buffer_flush(stdin);
        char input[6];
        fgets(input, 6, stdin);
        int number = atoi(input);
        if (!(number * 100000 <= wallet)) {
          puts("you do not have enough money to buy this item!");
          exit(0);
        } else {
          wallet = wallet - (number * 100000);
          puts("you bought our real flag!");
          printf("Money left in wallet: $%d\n", wallet);
          FILE *file = fopen("flag.txt", "r");

          
          if (file == NULL) {
            perror("Error opening file");
            return 1; 
          }
          
          int character;
          while ((character = fgetc(file)) != EOF) {
            putchar(character);
          }

          // Close the file
          fclose(file);
          exit(0);
        }
      } else if (option == 3) {
        puts("how many of the item do you want?");
        fflush(stdout);
        buffer_flush(stdin);
        char input[6];
        fgets(input, 6, stdin);
        int number = atoi(input);
        printf(
            "You have received %d free hats from YBN. Thank you for visiting "
            "our flag shop\n\n");
      } else {
        puts("invalid option! please try again");
      }
    } else if (option == 2) { // help menu
      puts("----help menu----");
      puts("[1] See an item's info");
      puts("[2] Get a free hint");
      fflush(stdout);
      buffer_flush(stdin);
      char input[2];
      fgets(input, 2, stdin);
      int option = atoi(input);
      if (option == 1){
        puts("YBN's Official fake flag: is a fake flag, cannot be traded for points, manufacturing cost is cheap so it costs less");
        puts("YBN's Official Real flag: is a real flag, can be traded for points, manufacturing cost is very high so it costs a lot");
        puts("YBN hat: is a hat, you can wear it, has a delivery time of 3-5 business days. Wearing it makes you look cool. Free swag frfrfrfrfrfr\n");
        fflush(stdout);
        buffer_flush(stdin);
        getchar();
      }
      else if (option == 2){
        system("xdg-open https://www.youtube.com/watch?v=vSKRVbVg6l4&list=PLQcpjwveNrhLk4gB6c87VACB9mBS0ibas&index=3");
        puts(":trollface:");
        exit(69420);
      }
      else{
        puts("invalid option! please try again!");
      }
    } else {
      puts("invalid option! please try again!");
    }
  }
  return 0;
}