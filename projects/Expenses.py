from random import randint

def rand_number():

    return randint(2000, 7000)

class ExpenseTracker:

    def __init__(self):
        self.expenses = {}

    def add_expense(self):
        expense_id = rand_number()
        description = input("Enter the description: ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))

        if expense_id in self.expenses:
            print(f"Expense ID {expense_id} already added.")
        else:
            self.expenses[expense_id] = {
                "expense_id": expense_id,
                "description": description,
                "category": category,
                "amount": amount
            }
            print(f"Expense ID {expense_id} added successfully.")

    def update_expenses(self):
        expense_id = int(input("Enter your expense_id: "))

        if expense_id in self.expenses:
            description = input("Enter the description: ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))

            self.expenses[expense_id] = {
                "expense_id": expense_id,
                "description": description,
                "category": category,
                "amount": amount
            }
            print(f"Expense ID {expense_id} updated.")
        else:
            print(f"Expense ID {expense_id} does not exist.")



    def delete_expense(self):

        expense_id = int(input("Enter the Expense ID: "))

        if expense_id in self.expenses:

            del self.expenses[expense_id]
            print(f"Expense ID: {expense_id} deleted successfully")

        else:
            print(f"Expense ID {expense_id} doesn't exist")


    def view_expenses(self):

        expense_id = int(input("Enter the Expense ID: "))
        if expense_id in self.expenses:

            expense = self.expenses[expense_id]

            print("\nView Expenses:")
            print(f"Description: {expense['description']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
        else:
            print(f"Expense ID {expense_id} does not exist.")



    def view_all(self):

        print("\n View All Expenses".upper())
        for key, value in self.expenses.items():

            print(value)
            print("_" * 20)

expense_tracker = ExpenseTracker()

while True:
    print("\nMain Menu:")
    print("1. Add Expenses")
    print("2. Update Expenses")
    print("3. View Expenses")
    print("4. Delete Expenses")
    print("5. View All Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        expense_tracker.add_expense()
    elif choice == "2":
        expense_tracker.update_expenses()
    elif choice == "3":
        expense_tracker.view_expenses()
    elif choice == "4":
        expense_tracker.delete_expense()
    elif choice == "5":
        expense_tracker.view_all()

    elif choice == "6":
        break
    else:

        print("Invalid Choice")