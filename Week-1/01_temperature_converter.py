"""Week 1 - Assignment 1: Temperature Converter.
Convert Celsius to Fahrenheit and Fahrenheit to Celsius using functions.
"""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Temperature Converter")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")

    try:
        choice = int(input("Choose an option (1/2): "))
        temperature = float(input("Enter temperature: "))

        if choice == 1:
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature:.2f} °C = {result:.2f} °F")
        elif choice == 2:
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature:.2f} °F = {result:.2f} °C")
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
