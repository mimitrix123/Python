"""Week 3 Assignment 3: Calculator class with exception handling."""


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Choose +, -, *, /: ").strip()
        operations = {
            "+": Calculator.add,
            "-": Calculator.subtract,
            "*": Calculator.multiply,
            "/": Calculator.divide,
        }
        if operation not in operations:
            raise ValueError("Invalid operation.")
        print("Result:", operations[operation](a, b))
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
