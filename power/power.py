def sequential_power(number : int, to: int) -> int:
    result = number
    for i in range(1, to):
        result *= number
    return result


def recursive_power(number : int, to: int) -> int:
    if to <= 1:
        return number
    
    return number * recursive_power(number, to - 1)

if __name__ == "__main__":
    
    print(sequential_power(
        number=int(input("Enter number : ")),
        to=int(input("to : "))
    ))

    print(recursive_power(
        number=int(input("Enter number : ")),
        to=int(input("to : "))
    ))
