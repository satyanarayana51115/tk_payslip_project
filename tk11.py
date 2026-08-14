import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Employee Payslip Generator")
root.geometry("950x750")
root.configure(bg="#f2f2f2")

# ------------------ HEADER SECTION ------------------
header_frame = tk.Frame(root, bg="#f2f2f2")
header_frame.pack(pady=10)

def add_header_row(label_text):
    frame = tk.Frame(header_frame, bg="#f2f2f2")
    frame.pack(fill="x", pady=3)
    label = tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), bg="#f2f2f2")
    label.pack(side="left", padx=(250, 10))
    entry = tk.Entry(frame, width=45)
    entry.pack(side="left")
    return entry

company_name_entry = add_header_row("Name of the Company:")
company_address_entry = add_header_row("Address of the Company:")
month_entry = add_header_row("Payslip for the Month of:")
emp_id_entry = add_header_row("ID of the Employee:")

# ------------------ LEFT FRAME (EMPLOYEE DETAILS) ------------------
left_frame = tk.LabelFrame(root, text="Employee Details", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
left_frame.place(x=40, y=150, width=420, height=280)

labels_left = ["Name", "Join Date", "Designation", "Department", "Level",
               "Location", "Effective Work Days", "Days in Month"]

entries_left = {}
for i, text in enumerate(labels_left):
    tk.Label(left_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=4, padx=10)
    entry = tk.Entry(left_frame, width=28)
    entry.grid(row=i, column=1, pady=4, padx=(40, 5))  # Added gap
    entries_left[text] = entry

# ------------------ RIGHT FRAME (BANK DETAILS) ------------------
right_frame = tk.LabelFrame(root, text="Bank & Statutory Details", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
right_frame.place(x=500, y=150, width=420, height=280)

labels_right = ["Bank Name", "Bank Account No", "PF No", "PF UAN",
                "ESI No", "PAN No", "LOP"]

entries_right = {}
for i, text in enumerate(labels_right):
    tk.Label(right_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=4, padx=10)
    entry = tk.Entry(right_frame, width=28)
    entry.grid(row=i, column=1, pady=4, padx=(40, 5))  # Added spacing
    entries_right[text] = entry

# ------------------ EARNINGS & DEDUCTIONS SECTION ------------------
earn_frame = tk.LabelFrame(root, text="Earnings & Deductions", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
earn_frame.place(x=40, y=450, width=880, height=250)

# Earnings Header
tk.Label(earn_frame, text="EARNINGS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=0, sticky="w", padx=10)
tk.Label(earn_frame, text="Full", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=1, padx=15)
tk.Label(earn_frame, text="Actual", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=2, padx=15)

earnings = ["Basic", "HRA", "Children Education Allowance", "Other Allowances"]
earn_entries = {}
for i, text in enumerate(earnings, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=5, padx=10)
    entry_full = tk.Entry(earn_frame, width=15)
    entry_full.grid(row=i, column=1, pady=5, padx=(30, 10))  # Added gap
    entry_actual = tk.Entry(earn_frame, width=15)
    entry_actual.grid(row=i, column=2, pady=5, padx=(20, 10))  # Added gap
    earn_entries[text] = (entry_full, entry_actual)

# Deductions Header
tk.Label(earn_frame, text="DEDUCTIONS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=4, sticky="w", padx=60)
tk.Label(earn_frame, text="Amount", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=5, padx=15)

deductions = ["PF", "ESI", "Professional Tax", "Others"]
deduct_entries = {}
for i, text in enumerate(deductions, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=4, sticky="w", pady=5, padx=60)
    entry = tk.Entry(earn_frame, width=15)
    entry.grid(row=i, column=5, pady=5, padx=(20, 10))  # Added gap
    deduct_entries[text] = entry

# ------------------ NET PAY SECTION ------------------
result_label = tk.Label(root, text="Net Pay: ₹ ________", font=("Arial", 12, "bold"), bg="#f2f2f2")
result_label.place(x=60, y=710)

root.mainloop()
