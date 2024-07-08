from expense import Expense


def main():
    # Welcome message
    print("Welcome To Your Expense Tracker!")

    # Get user input for an expense
    expense = get_user_expense()
    print(expense)

    # Uncomment the following lines to save and summarize expenses
    # save_user_expense_to_file()
    # summarize_user_expense()


def get_user_expense():
    # Get expense name from user
    expense_name = input("Enter expense name: \n")

    # Get expense amount from user and convert to float
    expense_amount = float(input("Enter expense amount: \n"))

    # List of expense categories
    expense_categories = [
        "🍔Food",
        "🏡Home",
        "💼Work",
        "🎉Fun",
        "✨Misc",
    ]

    # Prompt user to select a valid category
    while True:
        print("Select a category:")

        # Display the list of categories
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        # Define the valid range for input
        value_range = f"[1 - {len(expense_categories)}]"

        # Try to get a valid category number from user
        try:
            selected_index = int(input(f"Enter category number {value_range}\n")) - 1
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the selected index is within the valid range
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            # Create and return a new Expense object
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid selection. Please try again.")


def save_user_expense_to_file():
    # Placeholder for saving user expense to file
    pass


def summarize_user_expense():
    # Placeholder for summarizing user expenses
    pass


if __name__ == '__main__':
    main()