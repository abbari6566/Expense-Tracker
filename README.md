# Expense-Tracker

This is a simple Expense Tracker application built using Python and Tkinter, which allows users to:
- Add expenses with date, category, and amount
- View a list of added expenses in a tabular format
- Delete selected expenses from the list
- Automatically calculates and displays the total expenses

## Features
- **Add Expense**: Input the date, category, and amount, and click 'Add Expense' to save it.
- **View Expenses**: Click 'View Expenses' to display all recorded expenses.
- **Delete Expense**: Select an expense from the table and click 'Delete Expense' to remove it.
- **Total Expenses**: The total of all recorded expenses is automatically calculated and displayed.

## How to Run
1. Ensure you have Python installed.
2. Install Tkinter if it's not already available:

File Structure
expense_tracker.py: Main Python script for the expense tracker application.
expenses.txt: File used to store the recorded expenses.
Dependencies
Tkinter: For the graphical user interface.
os: To handle file operations like checking if the file exists.
