import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Payroll System")
root.geometry("550x550")  # window size

# Title
title_label = tk.Label(root, text="Payroll Management System", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Employee ID
emp_id_label = tk.Label(root, text="Employee ID :")
emp_id_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=1, column=1, pady=5)

# Employee Name
emp_name_label = tk.Label(root, text="Employee Name :")
emp_name_label.grid(row=2, column=0, sticky='e', padx=10, pady=5)
emp_name_entry = tk.Entry(root)
emp_name_entry.grid(row=2, column=1, pady=5)

# Department
dept_label = tk.Label(root, text="Department :")
dept_label.grid(row=3, column=0, sticky='e', padx=10, pady=5)
dept_entry = tk.Entry(root)
dept_entry.grid(row=3, column=1, pady=5)

# Designation
desig_label = tk.Label(root, text="Designation :")
desig_label.grid(row=4, column=0, sticky='e', padx=10, pady=5)
desig_entry = tk.Entry(root)
desig_entry.grid(row=4, column=1, pady=5)

# Basic Salary
emp_salary_label = tk.Label(root, text="Basic Salary (₹) :")
emp_salary_label.grid(row=5, column=0, sticky='e', padx=10, pady=5)
emp_salary_entry = tk.Entry(root)
emp_salary_entry.grid(row=5, column=1, pady=5)

# Result Display Box
result_box = tk.Text(root, height=12, width=60)
result_box.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Function to Calculate Salary
def calculate_salary():
    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    dept = dept_entry.get()
    desig = desig_entry.get()
    salary_text = emp_salary_entry.get()

    if not emp_id or not emp_name or not dept or not desig or not salary_text:
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    try:
        basic_salary = float(salary_text)
    except ValueError:
        messagebox.showerror("Error", "Salary must be a valid number.")
        return

    da = basic_salary * 0.10
    hra = basic_salary * 0.15
    tax = basic_salary * 0.05
    net_salary = basic_salary + da + hra - tax

    # Clear previous results
    result_box.delete(1.0, tk.END)

    # Display salary details in result box
    result_box.insert(tk.END,
                      f"Employee ID   : {emp_id}\n"
                      f"Employee Name : {emp_name}\n"
                      f"Department    : {dept}\n"
                      f"Designation   : {desig}\n"
                      f"Basic Salary  : ₹{basic_salary:.2f}\n"
                      f"DA (10%)      : ₹{da:.2f}\n"
                      f"HRA (15%)     : ₹{hra:.2f}\n"
                      f"Tax (5%)      : ₹{tax:.2f}\n"
                      f"------------------------------------\n"
                      f"Net Salary    : ₹{net_salary:.2f}")

# Calculate Button
button = tk.Button(root, text="Calculate Salary", command=calculate_salary, bg="lightblue", font=("Arial", 10, "bold"))
button.grid(row=7, column=0, columnspan=2, pady=10)

# Footer
footer = tk.Label(root, text="© 2025 Payroll System", font=('Arial', 8))
footer.grid(row=8, column=0, columnspan=2, pady=5)

# Adjust Column widths
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# Run GUI
root.mainloop()
