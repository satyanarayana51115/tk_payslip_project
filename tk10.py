import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Employee Payslip Generator")
root.geometry("900x700")
root.configure(bg="#f2f2f2")

# ------------------ Left Frame (Employee Details) ------------------
left_frame = tk.LabelFrame(root, text="Employee Details", padx=10, pady=10, bg="#f2f2f2")
left_frame.place(x=20, y=20, width=400, height=250)

labels_left = ["Name", "Join Date", "Designation", "Department", "Level",
               "Location", "Effective Work Days", "Days in Month"]

entries_left = {}
for i, text in enumerate(labels_left):
    tk.Label(left_frame, text=text, bg="#f2f2f2").grid(row=i, column=0, sticky="w", pady=3)
    entry = tk.Entry(left_frame, width=25)
    entry.grid(row=i, column=1, pady=3)
    entries_left[text] = entry

# ------------------ Right Frame (Bank Details) ------------------
right_frame = tk.LabelFrame(root, text="Bank & Statutory Details", padx=10, pady=10, bg="#f2f2f2")
right_frame.place(x=450, y=20, width=400, height=250)

labels_right = ["Bank Name", "Bank Account No", "PF No", "PF UAN",
                "ESI No", "PAN No", "LOP"]

entries_right = {}
for i, text in enumerate(labels_right):
    tk.Label(right_frame, text=text, bg="#f2f2f2").grid(row=i, column=0, sticky="w", pady=3)
    entry = tk.Entry(right_frame, width=25)
    entry.grid(row=i, column=1, pady=3)
    entries_right[text] = entry

# ------------------ Earnings & Deductions ------------------
earn_frame = tk.LabelFrame(root, text="Earnings & Deductions", padx=10, pady=10, bg="#f2f2f2")
earn_frame.place(x=20, y=300, width=830, height=250)

# Earnings Table
tk.Label(earn_frame, text="EARNINGS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=0)
tk.Label(earn_frame, text="Full", bg="#f2f2f2").grid(row=0, column=1)
tk.Label(earn_frame, text="Actual", bg="#f2f2f2").grid(row=0, column=2)

earnings = ["Basic", "HRA", "Children Education Allowance", "Other Allowances"]
earn_entries = {}
for i, text in enumerate(earnings, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2").grid(row=i, column=0, sticky="w", pady=3)
    entry = tk.Entry(earn_frame, width=10)
    entry.grid(row=i, column=1)
    entry2 = tk.Entry(earn_frame, width=10)
    entry2.grid(row=i, column=2)
    earn_entries[text] = (entry, entry2)

# Deductions
tk.Label(earn_frame, text="DEDUCTIONS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=4)
tk.Label(earn_frame, text="Amount", bg="#f2f2f2").grid(row=0, column=5)
deductions = ["PF", "ESI", "Professional Tax", "Others"]
deduct_entries = {}
for i, text in enumerate(deductions, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2").grid(row=i, column=4, sticky="w", pady=3)
    entry = tk.Entry(earn_frame, width=10)
    entry.grid(row=i, column=5)
    deduct_entries[text] = entry

# ------------------ Net Pay Section ------------------
result_label = tk.Label(root, text="Net Pay: ₹ ________", font=("Arial", 12, "bold"), bg="#f2f2f2")
result_label.place(x=20, y=580)

root.mainloop()
