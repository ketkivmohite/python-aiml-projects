import json
import datetime

# The file to store expense data
FILE_NAME = "expenses.json"

def load_expenses():
    """Loads expenses from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, start with an empty list
        return []

def save_expenses(expenses):
    """Saves the list of expenses to the JSON file."""
    with open(FILE_NAME, "w") as file:
        # indent=4 makes the JSON file human-readable
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Adds a new expense to the list."""
    print("\nEnter new expense details:")
    description = input("Description: ")

    # --- DATA VALIDATION ---
    # Loop until the user enters a valid number for the amount
    while True:
        try:
            amount = float(input("Amount: "))
            break # Exit the loop if conversion to float is successful
        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    # Automatically get today's date
    date = datetime.date.today().strftime("%Y-%m-%d")

    # Create the new expense as a dictionary
    new_expense = {
        "date": date,
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"\nExpense '{description}' added successfully!")

def view_expenses(expenses):
    """Displays all recorded expenses."""
    if not expenses:
        print("\nYour expense list is empty.")
        return

    print("\n--- Your Expenses ---")
    for expense in expenses:
        # The :.2f formats the number to two decimal places (like money)
        print(f"{expense['date']} - {expense['description']}: ₹{expense['amount']:.2f}")
    print("------------------------")

def calculate_total(expenses):
    """Calculates and displays the total of all expenses."""
    if not expenses:
        print("\nNo expenses to total.")
        return

    # A simple and efficient way to sum the 'amount' from each dictionary in the list
    total = sum(item['amount'] for item in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


# --- Main Program Loop ---
def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()