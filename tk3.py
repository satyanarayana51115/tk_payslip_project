import tkinter as tk
from tkinter import messagebox
# Main Window
root = tk.Tk()
root.title("Payroll System")
root.geometry("400x300")

# title Label
label = tk.Label(root, text="Payroll Management System", font=("Arial", 14, "bold"))
label.pack(pady=10)

# Employee ID
emp_id_label = tk.Label(root, text="Employee ID:")
emp_id_label.pack()
emp_id_entry = tk.Entry(root)
emp_id_entry.pack(pady=5)

# Employee Name
emp_name_label = tk.Label(root, text="Employee Name:")
emp_name_label.pack()
emp_name_entry = tk.Entry(root)
emp_name_entry.pack(pady=5)

# Basic Salary
emp_salary_label = tk.Label(root, text="Basic Salary (₹):")
emp_salary_label.pack()
emp_salary_entry = tk.Entry(root)
emp_salary_entry.pack(pady=5)

# Function to Display Details
def show_details():
    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    emp_salary = emp_salary_entry.get()

    if not emp_id or not emp_name or not emp_salary:
        messagebox.showwarning("Warning", "please fill all fields.")
        return
    
    messagebox.showinfo("Employee Details",
                        f"Employee ID  : {emp_id}\n"
                        f"Employee Name: {emp_name}\n"
                        f"Basic Salary : ₹{emp_salary}")

# Button
button = tk.Button(root, text="Show Details", command=show_details)
button.pack(pady=10)

# Run GUI
root.mainloop()