def showMenu():
    print("\n --- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expense")
    print("3. Show summary")
    print("4. Exit")
    return input("Choose an option: ")

def getExpenseDetails():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    return category, amount

def showExpenses(expenses):
    if not expenses:
        print("No expenses yet!")
        return
    print("\n--- Expenses ---")
    for e in expenses:
        print(f"{e['category']}: {e['amount']}")

def showSummary(totals):
    print("\n--- Sumamry by Category ---")
    for category, total in totals.items():
        print(f"{category} : {total}")

def showMessage(msg):
    print(f"\n✅ {msg}")
