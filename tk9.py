import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Employee Payslip System")
root.geometry("800x500")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Employee Payslip System", font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

# --- Main Frame divided into Left & Right sections ---
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=20, pady=10)

# Left Section (Employee Info)
left_frame = tk.LabelFrame(main_frame, text="Employee Details", padx=15, pady=10, font=('Arial', 10, 'bold'))
left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=5)

# Example fields (will add real ones later)
tk.Label(left_frame, text="Employee ID:").grid(row=0, column=0, sticky='e', pady=5)
tk.Entry(left_frame, width=25).grid(row=0, column=1, pady=5)

tk.Label(left_frame, text="Employee Name:").grid(row=1, column=0, sticky='e', pady=5)
tk.Entry(left_frame, width=25).grid(row=1, column=1, pady=5)

tk.Label(left_frame, text="Department:").grid(row=2, column=0, sticky='e', pady=5)
tk.Entry(left_frame, width=25).grid(row=2, column=1, pady=5)

tk.Label(left_frame, text="Designation:").grid(row=3, column=0, sticky='e', pady=5)
tk.Entry(left_frame, width=25).grid(row=3, column=1, pady=5)


# Right Section (Salary Details)
right_frame = tk.LabelFrame(main_frame, text="Salary Details", padx=15, pady=10, font=('Arial', 10, 'bold'))
right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=5)

# Example fields
tk.Label(right_frame, text="Basic Salary (₹):").grid(row=0, column=0, sticky='e', pady=5)
tk.Entry(right_frame, width=25).grid(row=0, column=1, pady=5)

tk.Label(right_frame, text="HRA (%):").grid(row=1, column=0, sticky='e', pady=5)
tk.Entry(right_frame, width=25).grid(row=1, column=1, pady=5)

tk.Label(right_frame, text="DA (%):").grid(row=2, column=0, sticky='e', pady=5)
tk.Entry(right_frame, width=25).grid(row=2, column=1, pady=5)

tk.Label(right_frame, text="Tax (%):").grid(row=3, column=0, sticky='e', pady=5)
tk.Entry(right_frame, width=25).grid(row=3, column=1, pady=5)


# Footer
footer = tk.Label(root, text="© 2025 Payroll System", font=('Arial', 8))
footer.pack(pady=5)

# Run the GUI
root.mainloop()
