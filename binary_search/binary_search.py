from typing import Union, List


def bable_sort(numbers: list) -> list:

    is_sorted = False

    for i in range(len(numbers)):

        if is_sorted:
            return numbers

        for j in range(len(numbers) - i):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_sorted = False
                continue

            is_sorted = False

    return numbers


def binary_search(numbers: List[int], number: int) -> Union[int, None]:

    min = 0
    max = len(numbers) - 1
    avarage = int()

    if number > numbers[max] or number < numbers[min]:
        return None

    while (min <= max):

        avarage = (max + min) // 2

        if number > numbers[avarage]:
            min = avarage + 1
        elif number < numbers[avarage]:
            max = avarage - 1
        else:
            return avarage

    return None


def main():

    num = int(input("enter number : "))
    numbers = list()
    for i in range(num):
        numbers.append(int(input(f"enter number for numbers {i + 1} : ")))


    numbers = bable_sort(numbers=numbers)
    print("numbers : ", numbers)

    number = int(input("number for find -> "))

    result = binary_search(numbers=numbers, number=number)

    if result is not None:
        print("founded , index : ", result)
    else:
        print("not found")


if __name__ == "__main__":
    main()
