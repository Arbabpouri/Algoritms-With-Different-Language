#include <stdio.h>
#include <stdbool.h>

void print_array(const int array[], const int arrayLen)
{
    // print int array[]

    for (int i = 0; i < arrayLen; i++)
    {
        printf("%d\t", array[i]);
    } // end for

    puts(" "); // print \n

} // print_array function

void bubble_sort(int numbers[], int arrayLen)
{
    // this function for bable sort
    int temp;
    bool is_sorted = true;

    for (int i = 0; i < arrayLen && is_sorted; i++)
    {
        for (int j = 0; j < arrayLen - i + 1; j++)
        {
            if (numbers[j] > numbers[j + 1])
            {
                temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
                is_sorted = false;
            } // end if

            is_sorted = true;

        } // end for

    } // end for

} // end bubble_sort function

void binary_search(const int numbers[], const int arrayLen, const int number)
{
    // this function for binary search

    int min = 0;
    int max = arrayLen - 1;
    int avvarage;

    if (number > numbers[max] || number < numbers[min]) // check number in my array or not
    {
        puts("yaft nashod");
    }

    else
    {

        while (min <= max)
        {
            avvarage = (max + min) / 2;
            if (number > numbers[avvarage])
            {
                min = avvarage + 1;
            } // end if
            else if (number < numbers[avvarage])
            {
                max = avvarage - 1;
            } // end else if
            else
            {
                printf("%s %d %s", "adad gofte shode dar index", avvarage, "ast");
                break;
            } // end else
        }

        if (min > max)
        {
            puts("yaft nashod");
        } // end if
    }
} // end binary_search function

int main(void)
{
    // this function for run my programm
    int len;
    printf("%s", "enter index number -> ");
    scanf("%d", &len); // get array len for define array

    int numbers[len];
    int selected;

    for (int i = 0; i < len; i++)
    {
        printf("%s %d %s", "index shomare", i, "ra bede -> ");
        scanf("%d", &numbers[i]); // get array indexs
    }                             // end for

    puts("berim baraye sort");

    bubble_sort(numbers, len); // call function for sort array

    print_array(numbers, len); // print all indexs

    printf("%s", "che adadi ra mikhay -> ");
    scanf("%d", &selected); // get number for search in array

    binary_search(numbers, len, selected); // call function for search
    puts(" ");                             // print \n

    return 0;

} // end programm
