def is_prime(number: int) -> bool:

    for i in range(2, number // 2 + 1):

        if number % i == 0:
            return False

    else:
        return True


def main():
    number = int(input("enter number : "))

    if is_prime(number=number):
        print("is prime")

    else:
        print("no prime")


if __name__ == "__main__":
    main()
