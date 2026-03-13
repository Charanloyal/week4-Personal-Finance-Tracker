from expense import Expense
from reports import monthly_total


def test_total():
    expenses = [
        Expense("2025", 10, "Food", "a"),
        Expense("2025", 20, "Travel", "b")
    ]

    assert monthly_total(expenses) == 30