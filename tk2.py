import tkinter as tk
from tkinter import messagebox # To show popup messages

# Main window
root = tk.Tk() 
root.title("Payroll System")
root.geometry("500x300")  

# Label
label = tk.Label(root, text="Payroll Management System")
label.pack(pady=10)  # Adds some space

# Entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Button action function
def show_entry():
    user_input = entry.get()   # Get text from Entry
    messagebox.showinfo("Your Input", f"You typed: {user_input}")

# Button
button = tk.Button(root, text="Click Me", command=show_entry)
button.pack(pady=10)

# Run GUI
root.mainloop()