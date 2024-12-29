def sequential_gcd(number_one: int, number_two: int) -> int:
    
    if number_one > number_two:
        number_one, number_two = number_two, number_one
    
    for i in range(number_one, 2, -1):
        if number_one % i == 0 and number_two % i == 0:
            return i
    
    return 1


def recursive_gcd(number_one: int, number_two: int) -> int:

    if number_two == 0:
        return number_one
    
    return recursive_gcd(number_two, number_one % number_two)
    

if __name__ == "__main__":
    print(sequential_gcd(
        number_one=int(input("Enter number one : ")),
        number_two=int(input("Enter number two : "))
    ))
    print(recursive_gcd(
        number_one=int(input("Enter number one : ")),
        number_two=int(input("Enter number two : "))
    ))
