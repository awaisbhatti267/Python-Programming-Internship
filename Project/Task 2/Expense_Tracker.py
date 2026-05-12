# Expense Tracker



total_expense = 0

def add_expense():
    global total_expense

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Expense must be greater than 0.")
            return

        total_expense += amount

        print(f"Expense added successfully.")
        print(f"Current Total: {total_expense}")

    except ValueError:
        print("Please enter a valid number.")


def remove_expense():
    global total_expense

    try:
        amount = float(input("Enter amount to remove: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > total_expense:
            print("Cannot remove more than total expenses.")
            return

        total_expense -= amount

        print(f"Expense removed successfully.")
        print(f"Current Total: {total_expense}")

    except ValueError:
        print("Please enter a valid number.")


def view_expense():
    print(f"\nTotal Expenses: {total_expense}\n")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        remove_expense()

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice. Try again.")