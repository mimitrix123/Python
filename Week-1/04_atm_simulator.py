"""Week 1 Mini Project: Simple ATM Simulator.
PIN-based login with balance, deposit, and withdrawal operations.
"""

CORRECT_PIN = "1234"
INITIAL_BALANCE = 5000.0
MAX_ATTEMPTS = 3


def check_balance(balance):
    print(f"Current balance: ₹{balance:.2f}")


def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: ₹"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return balance
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        check_balance(balance)
        return balance
    except ValueError:
        print("Please enter a valid amount.")
        return balance


def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
            check_balance(balance)
        return balance
    except ValueError:
        print("Please enter a valid amount.")
        return balance


def login():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        remaining = MAX_ATTEMPTS - attempt
        print(f"Incorrect PIN. Attempts remaining: {remaining}")
    return False


def atm():
    if not login():
        print("Too many incorrect attempts. Account locked.")
        return

    balance = INITIAL_BALANCE
    while True:
        print("\n===== SIMPLE ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    atm()
