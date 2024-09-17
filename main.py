import os
import tkinter as tk
from tkinter import ttk

# Function to add a new expense to the tracker
def add_expense():
    # Get the input values from the respective entry fields
    date = date_entry.get()
    category = category_entry.get()                                                                                                         
    amount = amount_entry.get()

    # Check if all fields are filled
    if date and category and amount:
        # Open the 'expenses.txt' file in append mode and write the new expense entry
        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{amount}\n")
        # Update the status label to show success
        status_label.config(text="Expense added successfully!", fg="green")
        # Clear the input fields after adding the expense
        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        # Refresh the view to display the newly added expense
        view_expenses()
    else:
        # If any field is empty, show an error message
        status_label.config(text="Please fill all the fields!", fg="red")

# Function to delete a selected expense from the tracker
def delete_expense():
    # Get the selected item from the treeview
    selected_item = expenses_tree.selection()
    if selected_item:
        # Retrieve the values (date, category, amount) from the selected row
        item_text = expenses_tree.item(selected_item, "values")
        date, category, amount = item_text
        # Read all lines from the file
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        # Rewrite the file excluding the deleted expense
        with open("expenses.txt", "w") as file:
            for line in lines:
                # Write back the line if it doesn't match the selected expense
                if line.strip() != f"{date},{category},{amount}":
                    file.write(line)
        # Update the status label to show success
        status_label.config(text="Expense deleted successfully!", fg="green")
        # Refresh the view to reflect the deletion
        view_expenses()
    else:
        # If no expense is selected, show an error message
        status_label.config(text="Please select an expense to delete!", fg="red")

# Function to display all expenses in the treeview
def view_expenses():
    global expenses_tree
    # Check if the expenses file exists
    if os.path.exists("expenses.txt"):
        total_expense = 0
        # Clear the current treeview data
        expenses_tree.delete(*expenses_tree.get_children())
        # Open the file and read each expense line
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                # Insert the expense data into the treeview
                expenses_tree.insert("", tk.END, values=(date, category, amount))
                total_expense += float(amount)
        # Update the total expense label
        total_label.config(text=f"Total Expense: {total_expense:.2f}")
    else:
        # If no expenses file exists, clear the treeview and set the total to 0
        total_label.config(text="No expenses recorded.")
        expenses_tree.delete(*expenses_tree.get_children())

# Initialize the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Create the labels and entry fields for date, category, and amount
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

# Button to add an expense, triggering the add_expense function
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Create a treeview to display expenses in tabular format
columns = ("Date", "Category", "Amount")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Category", text="Category")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Label to display the total expense
total_label = tk.Label(root, text="")
total_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Label to display the status of operations (add/delete)
status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Button to refresh and view all expenses
view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.grid(row=7, column=0, padx=5, pady=10)

# Button to delete the selected expense
delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=7, column=1, padx=5, pady=10)

# Ensure the expenses file exists; create it if not
if not os.path.exists("expenses.txt"):
    with open("expenses.txt", "w"):
        pass

# Display the current expenses when the application starts
view_expenses()

# Start the Tkinter event loop
root.mainloop()
