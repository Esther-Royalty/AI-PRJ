import json

FILENAME = "expenses.json"

try: 
    with open(FILENAME, "r") as file:
        all_expenses = json.load(file)
except FileNotFoundError:

 all_expenses = []


class BudgetTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()
        self.monthly_budget = float(input("Enter your monthly budget: "))

    def load_expenses(self):
     try: 
        with open(self.filename, "r") as file:
           return json.load(file)
     except FileNotFoundError:
        return []
        

    def add_expense(self, amount, category):
        new_expense = {"amount": amount, "category": category}
        self.expenses.append(new_expense)
    

    def save_expenses(self):
      try:
        with open(self.filename, "w") as file:
            save_expenses = json.dump(self.expenses, file)
      except Exception as e: 
         print("An error occured while saving expenses:", e)


    def get_total(self):
        total = 0
        for expense in self.expenses:
            total = total + expense["amount"]
        return total

    def check_budget(self):
       total = self.get_total()
       if total <= self.monthly_budget:
           remaining = self.monthly_budget - total
           print("You have this much left:", remaining)
       else:
           overspent = total - self.monthly_budget
           print("WARNING! You are over your budget by:", overspent)


# Using the class:
tracker = BudgetTracker()

# monthly_budget = float(input("Enter your monthly budget: "))

while True:
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (e.g. Food, Transport): ")
    tracker.add_expense(amount, category)
    print("Expense added!")

    go_on = input("Do you want to add another expense? (Yes/no): ")
    if go_on.lower() != "yes":
        break

tracker.save_expenses()
print("All expenses:", tracker.expenses)
print("Total spent:", tracker.get_total())
tracker.check_budget()





# while True:
#     expense_amount = float(input("Enter expense amount: "))
#     expense_category = input("Enter expense category (e.g. Food, Transport): ")

#     new_expense = {"amount": expense_amount, "category": expense_category}
#     all_expenses.append(new_expense)

#     print("Expense added!")

#     go_on = input("Do you want to add another expense? (Yes/no): ")
#     if go_on.lower()!= "yes":
#         break

# with open(FILENAME, "w") as file:
#     json.dump(all_expenses, file)
    
# total = 0
# for expense in all_expenses:
#     total = total + expense["amount"]

# print("All expenses:", all_expenses)
# print("Total spent:", total)

# if total <= monthly_budget:
#     remaining = monthly_budget - total
#     print("You have this much left:", remaining)
# else: 
#     overspent = total - monthly_budget
#     print("Warning! You are over your budget by:", overspent)