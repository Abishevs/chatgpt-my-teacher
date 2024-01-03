import tkinter as tk
from tkinter import ttk

def on_ttk_button_click():
    print("TTK Button Clicked")

root = tk.Tk()
root.title("Tkinter TTK Example")

ttk_label = ttk.Label(root, text="TTK Label")
ttk_label.pack(pady=10)

ttk_button = ttk.Button(root, text="TTK Button", command=on_ttk_button_click)
ttk_button.pack(pady=10)

ttk_entry = ttk.Entry(root)
ttk_entry.pack(pady=10)

root.mainloop()

