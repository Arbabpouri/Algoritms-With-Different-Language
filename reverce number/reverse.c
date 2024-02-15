#include <stdio.h>


int reverseNumber(int number)
{
    // this function for reverse number 
    int reversed;
    for (reversed = 0; number != 0 ; number /= 10)
    {
        reversed = (reversed * 10) + (number % 10);
    } // end for

    return reversed;
} // end reverseNumber function


int main(void)
{
    // my programm

    int number;
    
    printf("%s", "enter number for reverse : ");
    scanf("%d", &number); // get number from user

    int reversed = reverseNumber(number); // call function for reverse and save result data in reversed variable

    printf("number : %d --- reversed : %d\n", number, reversed); // print result

    return 0;

} // end main function
