from expense import Expense

def main():
    print("Welcome To Your  Expense Tracker ! ")

    # Get user input for expense
    expense = get_user_expense()
    print(expense)

    # Write their expenses to a file
    #save_user_expense_to_file()

    # Read file and summarize expenses
    #summarize_user_expense()


def get_user_expense():
   # print("Getting User Expense")
    expense_name = input("Enter expense name: \n")
    # Cast to a float
    expense_amount = float(input("Enter expense amount: \n"))

    expense_categories = [
        "🍔Food",
        "🏡Home",
        "💼Work",
        "🎉Fun",
        "✨Misc",
    ]

    #Keep repeating prompt until we get valid user input
    while True:
        print("Select a category:")
        # Show them the list of categories
        # 2 pull response index and item value
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        # Cast to int because input only takes in string
        # Subtract 1 because we added one
        # Error handling
        try:
            selected_index = int(input(f"Enter category number {value_range}\n")) - 1
        except ValueError:
            print("Invalid Input! Please enter a number")
            continue

        # 0 - 4
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense

        else:
            print("Invalid selection. Please try again.")

def save_user_expense_to_file():
    #print("Saving User Expense to file")
    pass

def summarize_user_expense():
    #print("Summarizing User Expense")
    pass


if __name__ == '__main__':
    main()
