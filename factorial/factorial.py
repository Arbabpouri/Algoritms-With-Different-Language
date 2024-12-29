def sequential_factorial(number: int) -> int:
    
    for i in range(number - 1, 1, -1):
        number *= i
    return number


def recursive_factorial(number: int) -> int:
    
    if 0 <= number <= 1:
        return 1
    
    return number * recursive_factorial(number - 1)
    

if __name__ == "__main__":
    print(sequential_factorial(int(input("Enter number : "))))
    print(recursive_factorial(int(input("Enter number : "))))