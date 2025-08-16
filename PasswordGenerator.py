import tkinter as tk
import random

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "Length should be above 4")
            return

        # Character sets
        upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = list("abcdefghijklmnopqrstuvwxyz")
        digits = list("0123456789")
        symbols = list("!@#$%^&*_-=|:,.<>?/")

        chars = upper + lower + digits + symbols
        password = ''.join(random.choice(chars) for _ in range(length))

        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)

    except ValueError:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Enter a valid number")

def clear_fields():
    length_entry.delete(0, tk.END)
    output_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("360x200")
root.resizable(False, False)

# Layout
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10, justify="center")
length_entry.pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)

output_entry = tk.Entry(root, width=35, justify="center")
output_entry.pack(pady=5)

# Clear button (placed after the output field)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

root.mainloop()
