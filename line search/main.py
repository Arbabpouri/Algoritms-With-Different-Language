from typing import List, Union


def line_search(numbers: List[int], number: int) -> Union[int, None]:
    
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    
    else:
        return None



def main() -> None:

    num = int(input("enter number : "))
    numbers = list()
    for i in range(num):
        numbers.append(int(input(f"enter number for numbers {i + 1} : ")))


    print("numbers : ", numbers)

    number = int(input("number for find -> "))

    result = line_search(numbers=numbers, number=number)

    if result is not None:
        print("founded , index : ", result)
    else:
        print("not found")


if __name__ == "__main__":
    main()
