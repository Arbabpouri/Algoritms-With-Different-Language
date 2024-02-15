#include <stdio.h>


void line_search(const int numbers[], const int arrayLen, const int number)
{

    // this function for line search algoritm

    for (int i = 0; i < arrayLen; i++)
    {
        if (number == numbers[i])
        {
            printf("adad yaft shode dar index %d ast\n", i);
            return ;
        } // end if
    }
    puts("yaft nashod");

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
        printf("index shomare %d ra vared konid -> ", i);
        scanf("%d", &numbers[i]); // get index
    } // end for

    printf("che adadi ru mikhay -> ");
    scanf("%d", &selected); // get number for search in array

    line_search(numbers, len ,selected); // call function for search in array
    puts(" "); // print \n
    
    return 0;

} // end main function
