import json
from pathlib import Path

dataFile = Path('data.json')

def loadExpenses():
    if dataFile.exists():
        with open(dataFile, "r") as f:
            return json.load(f)    
    return[]

def saveExpenses(expenses):
    with open(dataFile, 'w') as f:
        json.dump(expenses, f, indent=2)

def addExpense(expenses, category, amount):
    expenses.append({"category": category, "amount": amount})
    savaeExpenses(expenses)

def getTotalByCategory(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return[totals]