import model
import view

def main():
    expenses = model.loadExpenses()

    while True:
        choice = view.showMenu()

        if choice == "1":
            category, amount = view.getExpenseDetails()
            model.addExpense(expenses, category, amount)
            view.showMessage(f"Added {amount} to {category}")
        elif choice == "2":
            view.showExpenses(expenses)
        elif choice == "3":
            totals = model.getTotalByCategory(expenses)
            view.showSummary(totals)
        elif choice == "4":
            break
        else:
            view.showMessage("Invalid Choice!")

if __name__ == "__main__":
    main()