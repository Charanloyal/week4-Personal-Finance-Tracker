from collections import defaultdict


def category_summary(expenses):
    summary = defaultdict(float)

    for e in expenses:
        summary[e.category] += e.amount

    return summary


def monthly_total(expenses):
    total = 0
    for e in expenses:
        total += e.amount
    return total


def print_report(expenses):
    print("\n--- Expense Report ---")

    total = monthly_total(expenses)
    print("Total spent:", total)

    summary = category_summary(expenses)

    print("\nCategory Breakdown")
    for category, amount in summary.items():
        print(f"{category}: {amount}")