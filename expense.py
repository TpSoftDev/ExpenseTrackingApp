class Expense:
    # Represents an expense.

    def __init__(self, name, category, amount):
        # Initializes the expense with a name, category, and amount.
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        # Returns a string representation of the expense.
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"