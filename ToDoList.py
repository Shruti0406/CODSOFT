import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        mark = "✅" if t["done"] else "❌"
        listbox.insert(tk.END, f"{mark} {t['task']}")

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Empty", "Enter a task.")

def complete_task():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]]["done"] = True
        update_listbox()
    else:
        messagebox.showwarning("Select", "Choose a task to mark as completed.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Select", "Choose a task to delete.")

def update_task():
    selected = listbox.curselection()
    new_text = entry.get().strip()
    if selected and new_text:
        tasks[selected[0]]["task"] = new_text
        entry.delete(0, tk.END)
        update_listbox()
    elif not selected:
        messagebox.showwarning("Select", "Choose a task to update.")
    else:
        messagebox.showwarning("Empty", "Enter updated task text.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10, fill=tk.X)

tk.Button(root, text="Add Task", command=add_task).pack(pady=3)
tk.Button(root, text="Update Task", command=update_task).pack(pady=3)
tk.Button(root, text="Mark Completed", command=complete_task).pack(pady=3)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=3)

listbox = tk.Listbox(root, font=("Arial", 12), height=10)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.geometry("400x400")
root.mainloop()
