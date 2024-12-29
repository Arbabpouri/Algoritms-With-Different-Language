def sequential_fibonachi(number: int) -> int:
    if number == 0:
        return -1
    elif number == 1:
        return 0
    
    first = 0
    second = 1
    result = 1

    for i in range(2, number):
        result = second + first
        first = second
        second = result

    return result


def recursive_fibonachi(number: int) -> int:
    
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return recursive_fibonachi(number - 1) + recursive_fibonachi(number - 2)

if __name__ == "__main__":
    print(sequential_fibonachi(int(input("Enter number : "))))
    print(recursive_fibonachi(int(input("Enter number : "))))
