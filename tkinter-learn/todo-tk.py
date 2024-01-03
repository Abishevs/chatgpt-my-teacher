import tkinter as tk
from tkinter import ttk, filedialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with TTK")
        
        self.task_list = []
        
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.label = ttk.Label(self.frame, text="Enter task:")
        self.label.grid(row=0, column=0, sticky=tk.W)
        
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=1)
        
        self.add_button = ttk.Button(self.frame, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=2)
        
        self.remove_button = ttk.Button(self.frame, text="Remove", command=self.remove_task)
        self.remove_button.grid(row=0, column=3)
        
        self.tree = ttk.Treeview(self.frame)
        self.tree["columns"] = ("Tasks")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Tasks", anchor=tk.W, width=150)
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Tasks", text="Tasks", anchor=tk.W)
        
        self.tree.grid(row=1, columnspan=4)
        
    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_list.append(task)
            self.tree.insert(parent="", index="end", iid=len(self.task_list), text="", values=(task,))
            self.entry.delete(0, tk.END)
    
    def remove_task(self):
        selected = self.tree.selection()
        for task_id in selected:
            task = self.tree.item(task_id)["values"][0]
            self.task_list.remove(task)
            self.tree.delete(task_id)

if __name__ == "__main__":
    # root = tk.Tk()
    # app = TodoApp(root)
    # root.mainloop()
    filedialog.test()

