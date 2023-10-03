import json

# File to store budget data
BUDGET_FILE = "budget.json"

def load_budget():
    try:
        with open(BUDGET_FILE, "r") as file:
            budget = json.load(file)
    except FileNotFoundError:
        budget = {
            "income": [],
            "expenses": []
        }
    return budget

def save_budget(budget):
    with open(BUDGET_FILE, "w") as file:
        json.dump(budget, file)

def calculate_budget(budget):
    total_income = sum(item["amount"] for item in budget["income"])
    total_expenses = sum(item["amount"] for item in budget["expenses"])
    return total_income - total_expenses

def list_income_and_expenses(budget):
    print("Income:")
    for i, income in enumerate(budget["income"], start=1):
        print(f"{i}. {income['description']}: ${income['amount']}")

    print("\nExpenses:")
    for i, expense in enumerate(budget["expenses"], start=1):
        print(f"{i}. {expense['description']}: ${expense['amount']}")

def add_income(budget, description, amount):
    budget["income"].append({"description": description, "amount": amount})

def add_expense(budget, description, amount):
    budget["expenses"].append({"description": description, "amount": amount})

def analyze_expenses(budget):
    total_expenses = sum(item["amount"] for item in budget["expenses"])
    print(f"Total Expenses: ${total_expenses}")

def main():
    budget = load_budget()

    while True:
        print("\nOptions:")
        print("1. List income and expenses")
        print("2. Add income")
        print("3. Add expense")
        print("4. Calculate budget")
        print("5. Analyze expenses")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_income_and_expenses(budget)
        elif choice == "2":
            description = input("Enter income description: ")
            amount = float(input("Enter income amount: "))
            add_income(budget, description, amount)
            save_budget(budget)
        elif choice == "3":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(budget, description, amount)
            save_budget(budget)
        elif choice == "4":
            budget_balance = calculate_budget(budget)
            print(f"Budget Balance: ${budget_balance}")
        elif choice == "5":
            analyze_expenses(budget)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
