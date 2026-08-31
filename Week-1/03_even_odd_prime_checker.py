"""Week 1 - Assignment 3: Even/Odd and Prime Number Checker."""


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    try:
        number = int(input("Enter an integer: "))
        print(f"{number} is Even." if is_even(number) else f"{number} is Odd.")
        print(f"{number} is Prime." if is_prime(number) else f"{number} is not Prime.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
