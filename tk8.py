import tkinter as tk
from tkinter import messagebox

# --- Main Window ---
root = tk.Tk()
root.title("Payroll Management System")
root.geometry("650x550")

# --- Title ---
title_label = tk.Label(root, text="Payroll Management System", font=('Arial', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Employee Details ---
labels = [
    "Employee ID", "Employee Name", "Department", "Designation",
    "Basic Salary (₹)", "HRA (%)", "DA (%)", "TA (₹)", "Allowance (₹)",
    "PF (%)", "ESI (%)", "PT (₹)", "Other Deduction (₹)"
]

entries = {}

for i, label_text in enumerate(labels, start=1):
    label = tk.Label(root, text=f"{label_text}:", font=('Arial', 10))
    label.grid(row=i, column=0, sticky='e', padx=10, pady=5)

    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, pady=5)
    entries[label_text] = entry


# --- Function to Calculate Salary ---
def calculate_salary():
    try:
        # Basic employee info
        emp_id = entries["Employee ID"].get()
        emp_name = entries["Employee Name"].get()
        dept = entries["Department"].get()
        desg = entries["Designation"].get()

        # Salary components
        basic = float(entries["Basic Salary (₹)"].get() or 0)
        hra_per = float(entries["HRA (%)"].get() or 0)
        da_per = float(entries["DA (%)"].get() or 0)
        ta = float(entries["TA (₹)"].get() or 0)
        allowance = float(entries["Allowance (₹)"].get() or 0)
        pf_per = float(entries["PF (%)"].get() or 0)
        esi_per = float(entries["ESI (%)"].get() or 0)
        pt = float(entries["PT (₹)"].get() or 0)
        other_ded = float(entries["Other Deduction (₹)"].get() or 0)

        if not emp_id or not emp_name:
            messagebox.showwarning("Warning", "Please fill Employee ID and Name.")
            return

        # --- Calculations ---
        hra = basic * (hra_per / 100)
        da = basic * (da_per / 100)
        pf = basic * (pf_per / 100)
        esi = basic * (esi_per / 100)

        gross_salary = basic + hra + da + ta + allowance
        total_deductions = pf + esi + pt + other_ded
        net_salary = gross_salary - total_deductions

        # --- Display Results ---
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, f"--- PAYROLL SLIP ---\n")
        result_box.insert(tk.END, f"Employee ID   : {emp_id}\n")
        result_box.insert(tk.END, f"Employee Name : {emp_name}\n")
        result_box.insert(tk.END, f"Department    : {dept}\n")
        result_box.insert(tk.END, f"Designation   : {desg}\n")
        result_box.insert(tk.END, f"\n--- EARNINGS ---\n")
        result_box.insert(tk.END, f"Basic Salary  : ₹{basic:.2f}\n")
        result_box.insert(tk.END, f"HRA ({hra_per}%)    : ₹{hra:.2f}\n")
        result_box.insert(tk.END, f"DA ({da_per}%)     : ₹{da:.2f}\n")
        result_box.insert(tk.END, f"TA (Travel)   : ₹{ta:.2f}\n")
        result_box.insert(tk.END, f"Allowance     : ₹{allowance:.2f}\n")
        result_box.insert(tk.END, f"\n--- DEDUCTIONS ---\n")
        result_box.insert(tk.END, f"PF ({pf_per}%)      : ₹{pf:.2f}\n")
        result_box.insert(tk.END, f"ESI ({esi_per}%)     : ₹{esi:.2f}\n")
        result_box.insert(tk.END, f"PT (Professional Tax): ₹{pt:.2f}\n")
        result_box.insert(tk.END, f"Other Deductions    : ₹{other_ded:.2f}\n")
        result_box.insert(tk.END, f"-----------------------------\n")
        result_box.insert(tk.END, f"Gross Salary  : ₹{gross_salary:.2f}\n")
        result_box.insert(tk.END, f"Total Deductions: ₹{total_deductions:.2f}\n")
        result_box.insert(tk.END, f"Net Salary    : ₹{net_salary:.2f}\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in salary fields.")


# --- Calculate Button ---
calc_button = tk.Button(root, text="Calculate Salary", font=('Arial', 10, 'bold'),
                        bg="#4CAF50", fg="white", command=calculate_salary)
calc_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=15)

# --- Result Box ---
result_box = tk.Text(root, height=12, width=65, relief='solid', borderwidth=1)
result_box.grid(row=len(labels)+2, column=0, columnspan=2, padx=10, pady=10)

# --- Footer ---
footer = tk.Label(root, text="© 2025 Payroll System", font=('Arial', 9))
footer.grid(row=len(labels)+3, column=0, columnspan=2, pady=5)

# --- Run GUI ---
root.mainloop()
