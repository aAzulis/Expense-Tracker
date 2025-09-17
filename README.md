# 📊 Expense Tracker

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple command-line **Expense Tracker** built in Python.  
It allows you to **add expenses**, **view all expenses**, and **see a summary by category** — with data saved persistently in a JSON file.

---

## ✨ Features
- Add expenses with category and amount  
- View all saved expenses  
- Persistent storage using JSON  
- Summary of expenses by category  
- Clean architecture (MVP pattern)

---

## 📂 Project Structure
expense-tracker/
├── images/ # Screenshots for README
│ ├── preview.png
│ ├── preview1.png
│ └── preview2.png
├── model.py # Data logic (JSON read/write, calculations)
├── view.py # User interface (CLI input/output)
├── presenter.py # Program flow (connects Model & View)
├── requirements.txt # Dependencies (minimal)
├── data.json # Expense storage (auto-generated)
└── README.md # Project description


---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/aAzulis/Expense-Tracker.git
   cd Expense-Tracker

2. **Create a virtual enviroment**
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate # Windows

3. **Install dependecies**
    pip install -r requirements.txt

4. **Run the program**
    python presenter.py

## 🖥️ Example Usage
![Expense Tracker Screenshot](images/preview.png) 
![Expense Tracker Screenshot](images/preview1.png) 
![Expense Tracker Screenshot](images/preview2.png)

## 🏗️ MVP Brekdown
-Model → Handles expense storage and calculations

-View → Handles input/output with the user

-Presenter → Core logic connecting Model and View

## 📌 Future Improvements
-Add timestamps for expenses

-Generate charts

-Filter/search expenses by category or date

-Add unit tests for reliability

## 📜 License
This project is open-source under the **MIT Lincense**