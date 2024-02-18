def reverse_number(number: int) -> int:
    _reversed_number = 0

    while (number != 0):

        _reversed_number = (_reversed_number * 10) + (number % 10)
        number //= 10

    return _reversed_number


def main() -> None:

    number = int(input("number for find -> "))
    number_reversed = reverse_number(number=number)
    print(number_reversed)


if __name__ == "__main__":
    main()
