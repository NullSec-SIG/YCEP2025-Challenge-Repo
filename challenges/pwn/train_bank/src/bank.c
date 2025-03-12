#include <stdio.h>
#include <stdint.h>

void deposit(int32_t *balance, int32_t amount) {
    *balance += amount;
    printf("Deposited %d, current balance: %d\n", amount, *balance);
}

void withdraw(int32_t *balance, int32_t amount) {
    if (*balance < amount) {
        printf("Not enough balance!\n");
        return;
    }
    *balance -= amount;
    printf("Withdrew %d, current balance: %d\n", amount, *balance);
}

int main() {
    int32_t balance = 0;
    int32_t amount;

    printf("Welcome to the Bank!\n");

    while (1) {
        printf("Enter amount to deposit: ");
        scanf("%d", &amount);
        
        deposit(&balance, amount);

        // Check for overflow condition
        if (balance < 0) {
            printf("Overflow detected! Balance is negative.\n");

            // Reveal the flag when overflow occurs
            printf("Flag: YCEP25{successful_overflow}\n");
            break;  // End the loop after overflow to show flag
        }

        printf("Enter amount to withdraw: ");
        scanf("%d", &amount);

        withdraw(&balance, amount);
    }

    return 0;
}
