from expense import Expense
import datetime
import calendar

def main():
    # Welcome message
    print("Welcome To Your Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for an expense
    expense = get_user_expense()

    # Write their expense to a file
    save_user_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses
    summarize_user_expense(expense_file_path, budget)

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

def save_user_expense_to_file(expense, expense_file_path):
    # Print a message indicating the expense is being saved
    print(f"Saving User Expense : {expense} to {expense_file_path}")
    # Open the file in append mode (creates the file if it doesn't exist)
    with open(expense_file_path, "a") as f:
        # Write the expense details to the file
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_user_expense(expense_file_path, budget):
    # Print a message indicating the expenses are being summarized
    print(f"Summarizing User Expense : {expense_file_path}")
    expenses = []
    # Open the file in read mode
    with open(expense_file_path, "r") as f:
        # Read all lines from the file
        lines = f.readlines()
        for line in lines:
            # Split each line into expense details
            expense_name, expense_category, expense_amount = line.strip().split(",")
            # Create an Expense object and add it to the list
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    # Group Expenses by category
    # Data Structure: Dictionary - Look up Item using its key.
    # Key: Category name (5 Items in dictionary)
    # Value: Running Total of how much user has spent per category.
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount  # Starting Value

    # Print expenses by category
    print("Expenses by category")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount: .2f}")

    # Calculate and print total spent
    total_spent = sum([x.amount for x in expenses])
    print(f"\nTotal Spent: ${total_spent:.2f}")

    # Calculate and print remaining budget
    remaining_budget = budget - total_spent
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    # Daily Budget
    # Get the current date
    current_date = datetime.date.today()
    # Get the last day of the current month
    _, last_day = calendar.monthrange(current_date.year, current_date.month)
    # Calculate the remaining days in the current month
    remaining_days = last_day - current_date.day
    print(f"The remaining number of days in the current month is: {remaining_days}")
    # Calculate and print daily budget
    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget Per Day: ${daily_budget:.2f}"))

# Function to return green-colored text for terminal output
def green(text):
    return f"\033[32m{text}\033[0m"

if __name__ == '__main__':
    main()