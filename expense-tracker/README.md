Python Expense Tracker
A command-line application built with Python to help users track their daily expenses. This tool allows for adding new expenses with a description and amount, viewing a list of all past expenses, and calculating the total expenditure.

All data is saved to a expenses.json file, ensuring that the information persists between sessions. The application is localized to display currency in Indian Rupees (₹).

Features
Add Expense: Add a new expense with a description and a monetary amount.

Data Validation: Ensures that the amount entered is always a valid number.

View All Expenses: Displays a formatted list of all recorded expenses, including the date, description, and amount.

Calculate Total: Automatically calculates and displays the sum of all recorded expenses.

Data Persistence: All expense data is saved to a expenses.json file and is loaded automatically when the application starts.

Key Concepts Learned
Data Validation (try...except): Implemented robust error handling to manage non-numeric input for expense amounts, forcing the user to re-enter valid data.

Data Aggregation (sum()): Used a Python generator expression within the sum() function for an efficient way to calculate the total from a list of dictionaries.

Date and Time (datetime): Utilized the datetime module to automatically capture and format the current date for each new expense.

Structured Data (JSON): Handled the saving and loading of structured data (a list of dictionaries) using the json library.