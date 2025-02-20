using System;
using System.IO;
using System.Threading;

namespace LionExchange2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int balance = 1000;

            bool stop = false;
            while (stop == false)
            {
                Console.WriteLine();
                Console.WriteLine("Welcome to the LionExchange");
                Console.WriteLine("What would you like to do?");
                Console.WriteLine("1. Check balance");
                Console.WriteLine("2. Buy NVIDIA stocks");
                Console.WriteLine("3. Pray to Jensen Huang for flag");
                Console.WriteLine("4. Exit");

                int choice;
                Console.Write("Your choice: ");
                if (Int32.TryParse(Console.ReadLine(), out choice))
                {
                    Console.WriteLine();
                    switch (choice)
                    {
                        case 1:
                            Console.WriteLine($"Your current balance is ${balance}.");
                            break;

                        case 2:
                            Console.WriteLine($"Your current balance is ${balance}.");
                            Console.Write($"Each NVIDIA stock costs $126. How many would you like to buy? ");

                            int quantity = 0;
                            if (Int32.TryParse(Console.ReadLine(), out quantity))
                            {
                                if (quantity == 0)
                                {
                                    Console.WriteLine("Bye!");
                                    break;
                                }
                                else if (balance < quantity * 126)
                                {
                                    Console.WriteLine("You do not have enough money to buy that many stocks.");
                                }
                                else if (quantity > 0)
                                {
                                    balance -= quantity * 126;
                                    Console.WriteLine($"You have successfully bought ${quantity * 126} worth of NVIDIA stocks. The more you buy, the more you save!!!");
                                    Console.WriteLine("Jensen will be very happy.");
                                    Console.WriteLine($"Your new balance is ${balance}.");
                                }
                                else
                                {
                                    Console.WriteLine("Jensen: Hohoho! I see you tried to trick me with negative numbers. Nope, that no longer works, it's been patched now.");
                                }
                            }
                            break;

                        case 3:
                            Console.WriteLine("The more you buy, the more you save.");
                            Thread.Sleep(1000);
                            Console.WriteLine("The more you buy, the more you save.");
                            Thread.Sleep(1000);
                            Console.WriteLine("The more you buy, the more you save.");
                            Thread.Sleep(2000);

                            if (balance < 10000000)
                            {
                                Console.WriteLine("Jensen Huang: You aren't rich enough. I can tell you haven't bought enough of my stocks.");
                            }
                            else
                            {
                                string flag = File.ReadAllText("flag.txt");
                                Console.WriteLine($"Jensen Huang: Thanks for buying my stocks! Here's the flag: {flag}");
                                Console.WriteLine("Don't forget to buy my GPUs!");
                                stop = true;
                            }
                            break;

                        case 4:
                            Console.WriteLine("Goodbye!");
                            stop = true;
                            break;

                        default:
                            Console.WriteLine("Invalid input. Please enter a valid number.");
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid number.");
                }
            }
        }
    }
}
