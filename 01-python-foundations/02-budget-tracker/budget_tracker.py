import json

FILENAME = "expenses.json"

try: 
    with open(FILENAME, "r") as file:
        all_expenses = json.load(file)
except FileNotFoundError:

 all_expenses = []

monthly_budget = float(input("Enter your monthly budget: "))



while True:
    expense_amount = float(input("Enter expense amount: "))
    expense_category = input("Enter expense category (e.g. Food, Transport): ")

    new_expense = {"amount": expense_amount, "category": expense_category}
    all_expenses.append(new_expense)

    print("Expense added!")

    go_on = input("Do you want to add another expense? (Yes/no): ")
    if go_on.lower()!= "yes":
        break

with open(FILENAME, "w") as file:
    json.dump(all_expenses, file)
    
total = 0
for expense in all_expenses:
    total = total + expense["amount"]

print("All expenses:", all_expenses)
print("Total spent:", total)

if total <= monthly_budget:
    remaining = monthly_budget - total
    print("You have this much left:", remaining)
else: 
    overspent = total - monthly_budget
    print("Warning! You are over your budget by:", overspent)