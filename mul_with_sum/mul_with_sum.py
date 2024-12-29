def sequential_mul_with_sum(number: int, to: int) -> int:
    result = number
    for i in range(1, to):
        result += number
    
    return result
    

def recursive_mul_with_sum(number: int, to: int) -> int:
    
    if to <= 1:
        return number
    return number + recursive_mul_with_sum(number, to - 1)

if __name__ == "__main__":
    print(
        sequential_mul_with_sum(
            number=int(input("Enter number : ")),
            to=int(input("to : "))
        ))
    print(recursive_mul_with_sum(
        number=int(input("Enter number : ")),
        to=int(input("to : "))
    ))
