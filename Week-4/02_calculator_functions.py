"""Week 4 Practice 2: Calculator using functions."""


def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b): return "Cannot divide by zero" if b == 0 else a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


if __name__ == "__main__":
    x = float(input("First number: "))
    y = float(input("Second number: "))
    op = input("Operation (+,-,*,/): ")
    print("Result:", operations.get(op, lambda *_: "Invalid operation")(x, y))
