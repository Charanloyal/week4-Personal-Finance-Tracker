from expense import Expense
from expense_manager import ExpenseManager
from file_handler import save_expenses, load_expenses, backup_data
from reports import print_report
from utils import validate_amount


manager = ExpenseManager()


def add_expense():

    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")

    if not validate_amount(amount):
        print("Invalid amount")
        return

    category = input("Category: ")
    desc = input("Description: ")

    exp = Expense(date, amount, category, desc)
    manager.add_expense(exp)

    print("Expense added!")


def view_expenses():
    for i, e in enumerate(manager.expenses):
        print(i, e.date, e.amount, e.category, e.description)


def save_data():
    save_expenses(manager.to_list())


def load_data():
    data = load_expenses()
    manager.load_from_list(data)


def start_app():

    load_data()

    while True:
        print("\nPersonal Finance Tracker")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Reports")
        print("4 Backup")
        print("5 Save")
        print("6 Exit")

        choice = input("Select: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print_report(manager.expenses)

        elif choice == "4":
            backup_data()

        elif choice == "5":
            save_data()

        elif choice == "6":
            save_data()
            print("Goodbye")
            break

        else:
            print("Invalid choice")