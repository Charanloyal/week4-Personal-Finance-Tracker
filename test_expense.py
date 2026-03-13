from expense import Expense


def test_expense_creation():
    e = Expense("2025-01-01", 50, "Food", "Lunch")

    assert e.date == "2025-01-01"
    assert e.amount == 50
    assert e.category == "Food"
    assert e.description == "Lunch"