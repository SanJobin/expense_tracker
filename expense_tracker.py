"""
Expense Tracker System
Intermediate Python Activity
"""

FILE_NAME = "expenses.txt"


def add_expense():
    """Add a new expense to the file."""
    print("\n--- Add Expense ---")
    category = input("Enter category (e.g. Food, Travel, Shopping): ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

    print(f"Expense added: {category} - ₹{amount:.2f}")


def view_expenses():
    """Read and display all expenses from the file."""
    print("\n--- All Expenses ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expenses recorded yet.")
            return

        print(f"{'#':<5} {'Category':<15} {'Amount':>10}")
        print("-" * 32)

        for i, line in enumerate(lines, start=1):
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    category, amount = parts
                    try:
                        print(f"{i:<5} {category:<15} ₹{float(amount):>9.2f}")
                    except ValueError:
                        print(f"{i:<5} {category:<15} {'(invalid)':>10}")

    except FileNotFoundError:
        print("No expense file found. Please add an expense first.")


def calculate_total():
    """Calculate and display the total amount spent."""
    print("\n--- Total Expense ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        total = 0.0
        count = 0

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    try:
                        total += float(parts[1])
                        count += 1
                    except ValueError:
                        pass

        if count == 0:
            print("No expenses recorded yet.")
        else:
            print(f"Total expenses recorded : {count}")
            print(f"Total amount spent      : ₹{total:.2f}")

    except FileNotFoundError:
        print("No expense file found. Please add an expense first.")


def category_wise_count():
    """Count how many times each category appears."""
    print("\n--- Category-wise Count ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        category_count = {}

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    category = parts[0]
                    category_count[category] = category_count.get(category, 0) + 1

        if not category_count:
            print("No expenses recorded yet.")
            return

        print(f"{'Category':<15} {'Count':>8}")
        print("-" * 25)
        for category, count in sorted(category_count.items()):
            print(f"{category:<15} {count:>8}")

    except FileNotFoundError:
        print("No expense file found. Please add an expense first.")


def show_menu():
    """Display the main menu."""
    print("\n=============================")
    print("     EXPENSE TRACKER MENU    ")
    print("=============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category-wise Count")
    print("5. Exit")
    print("=============================")


def main():
    """Main function to run the expense tracker."""
    print("Welcome to the Expense Tracker!")

    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_wise_count()
        elif choice == "5":
            print("\nThank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
