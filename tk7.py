import tkinter as tk
from tkinter import messagebox

# --- Main Window ---
root = tk.Tk()
root.title("Payroll Management System")
root.geometry("550x700")

# --- Title ---
title_label = tk.Label(root, text="Payroll Management System", font=('Arial', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Employee Details ---
labels = ["Employee ID", "Employee Name", "Department", "Designation",
          "Basic Salary (₹)", "HRA (%)", "DA (%)", "Allowance (₹)", "Deduction (₹)"]

entries = {}

for i, label_text in enumerate(labels, start=1):
    label = tk.Label(root, text=f"{label_text}:", font=('Arial', 10))
    label.grid(row=i, column=0, sticky='e', padx=10, pady=5)

    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, pady=5)
    entries[label_text] = entry


# --- Function to Calculate Net Salary ---
def calculate_salary():
    try:
        emp_id = entries["Employee ID"].get()
        emp_name = entries["Employee Name"].get()
        dept = entries["Department"].get()
        desg = entries["Designation"].get()
        basic = float(entries["Basic Salary (₹)"].get() or 0)
        hra_per = float(entries["HRA (%)"].get() or 0)
        da_per = float(entries["DA (%)"].get() or 0)
        allowance = float(entries["Allowance (₹)"].get() or 0)
        deduction = float(entries["Deduction (₹)"].get() or 0)

        # Validations
        if not emp_id or not emp_name:
            messagebox.showwarning("Warning", "Please fill at least Employee ID and Name.")
            return

        # Calculations
        hra = basic * (hra_per / 100)
        da = basic * (da_per / 100)
        net_salary = basic + hra + da + allowance - deduction

        # Display in text box
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, f"--- Payroll Slip ---\n")
        result_box.insert(tk.END, f"Employee ID   : {emp_id}\n")
        result_box.insert(tk.END, f"Employee Name : {emp_name}\n")
        result_box.insert(tk.END, f"Department    : {dept}\n")
        result_box.insert(tk.END, f"Designation   : {desg}\n")
        result_box.insert(tk.END, f"\n--- Salary Details ---\n")
        result_box.insert(tk.END, f"Basic Salary  : ₹{basic:.2f}\n")
        result_box.insert(tk.END, f"HRA ({hra_per}%)    : ₹{hra:.2f}\n")
        result_box.insert(tk.END, f"DA ({da_per}%)     : ₹{da:.2f}\n")
        result_box.insert(tk.END, f"Allowance     : ₹{allowance:.2f}\n")
        result_box.insert(tk.END, f"Deduction     : ₹{deduction:.2f}\n")
        result_box.insert(tk.END, f"----------------------------\n")
        result_box.insert(tk.END, f"Net Salary    : ₹{net_salary:.2f}\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in salary fields.")


# --- Button ---
calc_button = tk.Button(root, text="Calculate Salary", font=('Arial', 10, 'bold'),
                        bg="#4CAF50", fg="white", command=calculate_salary)
calc_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=15)

# --- Result Box ---
result_box = tk.Text(root, height=12, width=60, relief='solid', borderwidth=1)
result_box.grid(row=len(labels)+2, column=0, columnspan=2, padx=10, pady=10)

# --- Footer ---
footer = tk.Label(root, text="© 2025 Payroll System", font=('Arial', 9))
footer.grid(row=len(labels)+3, column=0, columnspan=2, pady=5)

# --- Run GUI ---
root.mainloop()
