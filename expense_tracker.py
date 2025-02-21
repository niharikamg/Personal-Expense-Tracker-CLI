import argparse
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL,
                        category TEXT,
                        description TEXT,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(amount, category, description, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))
    conn.commit()
    conn.close()
    print(f"✅ Expense added: {amount} - {category} - {description} ({date})")

def view_expenses(period="all"):
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT * FROM expenses ORDER BY date DESC"
    df = pd.read_sql(query, conn)
    conn.close()

    if df.empty:
        print("⚠️ No expenses recorded yet.")
    else:
        print(df)

def export_data(format="csv"):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    if format == "csv":
        df.to_csv("expenses.csv", index=False)
        print("✅ Data exported to expenses.csv")
    elif format == "json":
        df.to_json("expenses.json", indent=4)
        print("✅ Data exported to expenses.json")

def plot_expenses():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT category, SUM(amount) as total FROM expenses GROUP BY category", conn)
    conn.close()

    if df.empty:
        print("⚠️ No expenses to display.")
    else:
        df.plot(kind="bar", x="category", y="total", legend=False, title="Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Personal Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help="Expense amount")
    add_parser.add_argument("category", type=str, help="Expense category")
    add_parser.add_argument("description", type=str, help="Expense description")
    add_parser.add_argument("date", type=str, help="Expense date (YYYY-MM-DD)")

    view_parser = subparsers.add_parser("view", help="View recorded expenses")

    export_parser = subparsers.add_parser("export", help="Export expenses data")
    export_parser.add_argument("--format", choices=["csv", "json"], default="csv", help="Export format")

    plot_parser = subparsers.add_parser("plot", help="Plot expense trends")

    args = parser.parse_args()

    init_db()

    if args.command == "add":
        add_expense(args.amount, args.category, args.description, args.date)
    elif args.command == "view":
        view_expenses()
    elif args.command == "export":
        export_data(args.format)
    elif args.command == "plot":
        plot_expenses()
