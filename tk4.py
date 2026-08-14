import tkinter as tk
from tkinter import messagebox

# Main Windown
root = tk.Tk()
root.title("Payroll System")
root.geometry("400x300")

# Title Label
label = tk.Label(root, text="Payroll Management System", font=('Arial', 14, 'bold'))
label.pack(pady=10)

# Employee ID
emp_id_label = tk.Label(root, text="Employee ID")
emp_id_label.pack(pady=5)
emp_id_entry = tk.Entry(root)
emp_id_entry.pack()

# Employee Name
emp_name_label = tk.Label(root, text="Employee Name")
emp_name_label.pack()
emp_name_entry = tk.Entry(root)
emp_name_entry.pack(pady=5)

# Basic Salary
emp_salary_label = tk.Label(root, text="Basic Salary (₹)")
emp_salary_label.pack()
emp_salary_entry = tk.Entry(root)
emp_salary_entry.pack(pady=5)

# Function to Calculate Net Salary
def calculate_salary():
    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    salary_text = emp_salary_entry.get()

    if not emp_id or not emp_name or not salary_text:
        messagebox.showwarning("Warning", "Please fill all fields.")
        return
    
    try:
        basic_salary = float(salary_text)
    except ValueError:
        messagebox.showerror("Error", "Salary must be a valid number.")
        return
    
    # Salary Components
    da = basic_salary * 0.10
    hra = basic_salary * 0.15
    tax = basic_salary * 0.05
    net_salary = basic_salary + da + hra - tax

    # Display Results
    messagebox.showinfo("Salary Calculation",
                        f"Employee ID   : {emp_id}\n"
                        f"Employee Name : {emp_name}\n"
                        f"Basic Salary  : ₹{basic_salary:.2f}\n"
                        f"DA (10%)      : ₹{da:.2f}\n"
                        f"HRA (15%)     : ₹{hra:.2f}\n"
                        f"Tax (5%)      : ₹{tax:.2f}\n"
                        f"---------------------------------\n"
                        f"Net Salary : ₹{net_salary:.2f}")
    
# Button
button = tk.Button(root, text="Calculate Salary", command=calculate_salary)
button.pack(pady=15)

# Run GUI
root.mainloop()