import json
import os

DATA_FILE = "expenses.json"


def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading file:", e)
        return []


def backup_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as src:
                data = src.read()

            with open("backup_expenses.json", "w") as dest:
                dest.write(data)

            print("Backup created successfully.")
    except Exception as e:
        print("Backup error:", e)