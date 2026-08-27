all_expenses = []

while True:
    expense_amount = float(input("Enter expense amount: "))
    expense_category = input("Enter expense category (e.g. Food, Transport): ")

    new_expense = {"amount": expense_amount, "category": expense_category}
    all_expenses.append(new_expense)

    print("Expense added!")

    go_on = input("Do you want to add another expense? (Yes/no): ")
    if go_on.lower()!= "yes":
        break

total = 0
for expense in all_expenses:
    total = total + expense["amount"]

print("All expenses:", all_expenses)
print("Total spent:", total)

print("All expenses:", all_expenses)