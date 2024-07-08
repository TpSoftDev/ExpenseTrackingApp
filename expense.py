class Expense:
    # Represents an expense.

    def __init__(self, name, category, amount):
        # Initializes name, category, and amount.
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        # Returns a string representation.
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"