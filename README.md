# Personal Expense Tracker CLI

## 📌 Description
A command-line tool to track and analyze personal expenses, helping users manage their budget efficiently.

## 🚀 Features
- Add, update, and delete expenses.
- Categorize expenses (Food, Transport, Rent, etc.).
- View expense summaries (daily, weekly, monthly).
- Save data in CSV, JSON, or SQLite database.
- Generate expense trend charts.

## 🛠 Requirements
Ensure you have **Python 3.6+** installed. Install dependencies with:
```sh
pip install pandas matplotlib sqlite3
```

## 📄 Usage
Run the script with the following commands:
```sh
python expense_tracker.py add 50 "Food" "Lunch at Subway" "2025-02-20"
python expense_tracker.py view
python expense_tracker.py export --format csv
python expense_tracker.py plot
```

## 📜 License
This project is open-source and available under the MIT License.

