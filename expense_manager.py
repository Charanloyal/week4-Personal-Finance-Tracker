from expense import Expense


class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def search_by_category(self, category):
        return [
            e for e in self.expenses
            if e.category.lower() == category.lower()
        ]

    def total_expenses(self):
        return sum(e.amount for e in self.expenses)

    def to_list(self):
        return [e.to_dict() for e in self.expenses]

    def load_from_list(self, data):
        self.expenses = [Expense.from_dict(d) for d in data]