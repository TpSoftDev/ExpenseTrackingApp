# Expense Tracker App

Welcome to the Expense Tracker! This program helps you track your expenses and manage your budget effectively. Whether you're trying to save money or simply understand where your money goes, this tool provides insights into your spending habits.

## Features

- **Expense Logging**: Record your expenses by entering the name, category, and amount spent.
- **Expense Categorization**: Choose from predefined categories like Food, Home, Work, Fun, and Misc to classify your expenses.
- **Budget Monitoring**: Set a monthly budget and track your spending against it.
- **Expense Summarization**: View a summary of your expenses categorized by type and see the total spent.
- **Daily Budget Calculation**: Automatically calculates your remaining budget per day based on the current month's remaining days.
- **Terminal UI**: Simple and intuitive command-line interface.

## Getting Started

1. **Installation**:
   - Clone the repository:
     ```bash
     git clone <repository_url>
     ```
   - Install dependencies if required.

2. **Usage**:
   - Run the program:
     ```bash
     python main.py
     ```
   - Follow the prompts to log your expenses and view summaries.

3. **Customization**:
   - Adjust the initial budget (`budget` variable in `main()` function) to match your financial goals.
   - Modify expense categories (`expense_categories` list in `get_user_expense()` function) to suit your spending habits.

## Example

Here's an example of how the Expense Tracker works:

1. **Logging an Expense**:
   - Enter the name of the expense (e.g., "Groceries").
   - Enter the amount spent (e.g., 50.00).
   - Select a category from the provided options.

2. **Viewing Summary**:
   - After logging expenses, the program summarizes your spending by category.
   - It calculates the total amount spent and compares it against your budget.
   - Displays the remaining budget and daily budget allowance.

3. **Repeat**:
   - Continue logging expenses throughout the month to track your spending habits effectively.
   - Use the daily budget calculation to manage your finances daily.

## Contributing

Contributions are welcome! If you have ideas for new features, find a bug, or want to improve the code or documentation, feel free to contribute by creating a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to customize this README further to match any additional features or nuances specific to your implementation. This should provide a comprehensive and appealing introduction to your Expense Tracker program on GitHub.