#include <stdio.h>


void line_search(const int numbers[], const int arrayLen, const int number)
{

    // this function for line search algoritm

    for (int i = 0; i < arrayLen; i++)
    {
        if (number == numbers[i])
        {
            printf("number founded , index : %d \n", i);
            return ;
        } // end if
    }
    puts("no founded");

} // end line_search function

int main(void)
{
    // this function for run my programm

    int len;
    int selected;

    printf("%s", "enter index number -> ");
    scanf("%d", &len); // get array len for define

    int numbers[len]; // define array with dynamic len

    for (int i = 0; i < len; i++)
    {
        printf("please enter number for index : %d -> ", i);
        scanf("%d", &numbers[i]); // get index
    } // end for

    printf("number for find -> ");
    scanf("%d", &selected); // get number for search in array

    line_search(numbers, len ,selected); // call function for search in array
    puts(" "); // print \n
    
    return 0;

} // end main function
