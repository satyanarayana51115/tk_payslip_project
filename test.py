import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")
frame = tk.Label(frame, text="Name:")
frame.grid(row=0, column=0, sticky="e", padx=10, pady=10)
frame = tk.Entry(frame)
frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)


root.mainloop()