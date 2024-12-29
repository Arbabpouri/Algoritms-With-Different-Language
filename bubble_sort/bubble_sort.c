#include <stdio.h>
#include <stdbool.h>

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

int main(void)
{

    int num;
    printf("%s", "enter index num -> ");
    scanf("%d", &num);

    int numbers[num];

    for (int i = 0; i < num; i++)
    {

        printf("%s %d %s", "please enter index : ", i, "--> ");
        scanf("%d", &numbers[i]);

    } // end for

    bubble_sort(numbers, num); // sort
    puts("array sorted");

    for (int i = 0; i < num; i++)
    {
        printf("%d\t", numbers[i]);
    } // end for

    puts(" "); // print \n

    return 0;

} // end main function
