import tkinter as tk

def on_button_click():
    print("Classic Tkinter Button Clicked")

root = tk.Tk()
root.title("Classic Tkinter Example")

label = tk.Label(root, text="Classic Tkinter Label")
label.pack(pady=10)

button = tk.Button(root, text="Classic Tkinter Button", command=on_button_click)
button.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

root.mainloop()

