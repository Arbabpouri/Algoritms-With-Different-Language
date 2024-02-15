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


def main():

    num = int(input("enter number : "))
    numbers = list()
    for i in range(num):
        numbers.append(int(input(f"enter number for numbers {i + 1} : ")))

    numbers = bable_sort(numbers=numbers)

    print(numbers)
