import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Employee Payslip Generator")
root.geometry("950x750")
root.configure(bg="#f2f2f2")

# Configure root grid for responsiveness
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# ------------------ HEADER SECTION ------------------
header_container = tk.Frame(root, bg="#f2f2f2")
header_container.grid(row=0, column=0, sticky="ew", pady=10)
header_container.columnconfigure(0, weight=1)

header_frame = tk.Frame(header_container, bg="#f2f2f2")
header_frame.grid(row=0, column=0)
header_frame.columnconfigure(0, weight=0)
header_frame.columnconfigure(1, weight=1)

def add_header_row(row, label_text):
    label = tk.Label(header_frame, text=label_text, font=("Arial", 10, "bold"), bg="#f2f2f2")
    label.grid(row=row, column=0, sticky="e", padx=10, pady=4)
    entry = tk.Entry(header_frame, width=60)
    entry.grid(row=row, column=1, sticky="ew", padx=10, pady=4)
    return entry

company_name_entry = add_header_row(0, "Name of the Company:")
company_address_entry = add_header_row(1, "Address of the Company:")
month_entry = add_header_row(2, "Payslip for the Month of:")
emp_id_entry = add_header_row(3, "ID of the Employee:")

# ------------------ MAIN DETAILS SECTION ------------------
main_details_frame = tk.Frame(root, bg="#f2f2f2")
main_details_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

main_details_frame.columnconfigure(0, weight=1)
main_details_frame.columnconfigure(1, weight=1)

# LEFT FRAME
left_frame = tk.LabelFrame(main_details_frame, text="Employee Details", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
left_frame.columnconfigure(1, weight=1)

labels_left = ["Name", "Join Date", "Designation", "Department", "Level",
               "Location", "Effective Work Days", "Days in Month"]

entries_left = {}
for i, text in enumerate(labels_left):
    tk.Label(left_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=4, padx=10)
    entry = tk.Entry(left_frame)
    entry.grid(row=i, column=1, sticky="ew", pady=4, padx=(60, 10))  # Increased left gap
    entries_left[text] = entry

# RIGHT FRAME
right_frame = tk.LabelFrame(main_details_frame, text="Bank & Statutory Details", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
right_frame.columnconfigure(1, weight=1)

labels_right = ["Bank Name", "Bank Account No", "PF No", "PF UAN",
                "ESI No", "PAN No", "LOP"]

entries_right = {}
for i, text in enumerate(labels_right):
    tk.Label(right_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=4, padx=10)
    entry = tk.Entry(right_frame)
    entry.grid(row=i, column=1, sticky="ew", pady=4, padx=(60, 10))  # Increased left gap
    entries_right[text] = entry

# ------------------ EARNINGS & DEDUCTIONS SECTION ------------------
earn_frame = tk.LabelFrame(root, text="Earnings & Deductions", padx=15, pady=10, bg="#f2f2f2", font=("Arial", 10, "bold"))
earn_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

for col in range(6):
    earn_frame.columnconfigure(col, weight=1)

tk.Label(earn_frame, text="EARNINGS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=0, sticky="w", padx=10)
tk.Label(earn_frame, text="Full", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=1)
tk.Label(earn_frame, text="Actual", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=2)

earnings = ["Basic", "HRA", "Children Education Allowance", "Other Allowances"]
earn_entries = {}
for i, text in enumerate(earnings, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=0, sticky="w", pady=5, padx=10)
    entry_full = tk.Entry(earn_frame)
    entry_full.grid(row=i, column=1, sticky="ew", pady=5, padx=10)
    entry_actual = tk.Entry(earn_frame)
    entry_actual.grid(row=i, column=2, sticky="ew", pady=5, padx=10)
    earn_entries[text] = (entry_full, entry_actual)

tk.Label(earn_frame, text="DEDUCTIONS", font=("Arial", 10, "bold"), bg="#f2f2f2").grid(row=0, column=4, sticky="w", padx=30)
tk.Label(earn_frame, text="Actual", font=("Arial", 9, "bold"), bg="#f2f2f2").grid(row=0, column=5)

deductions = ["PF", "ESI", "Professional Tax", "Others"]
deduct_entries = {}
for i, text in enumerate(deductions, start=1):
    tk.Label(earn_frame, text=text, bg="#f2f2f2", font=("Arial", 9)).grid(row=i, column=4, sticky="w", pady=5, padx=10)
    entry = tk.Entry(earn_frame)
    entry.grid(row=i, column=5, sticky="ew", pady=5, padx=10)
    deduct_entries[text] = entry

# ------------------ NET PAY SECTION ------------------
result_label = tk.Label(root, text="Net Pay: ₹ ________", font=("Arial", 12, "bold"), bg="#f2f2f2")
result_label.grid(row=3, column=0, sticky="w", padx=40, pady=10)

root.mainloop()
