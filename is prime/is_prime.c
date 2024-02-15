#include <stdio.h>
#include <stdbool.h>

bool is_prime(int); // is_prime function prototype

int main(void) 
{ 
    // main function for run my programm
    int number;
    printf("%s", "Enter number for check prime -> ");
    scanf("%d", &number); // get number from user

    if (is_prime(number)) // check is_prime() function result
    {
        puts("number is prime"); // if true
    }
    else
    {
        puts("number not prime"); // if false
    }
} // end function main

bool is_prime(int number)
{
    // is_prime function for check numbers whitch they are prime or not
    
    for (int i = 2; i <= number / 2; i++)
    {
        if (number % i == 0)
        {
            return false;
        }
    }
    return true;
} // end is_prime function
