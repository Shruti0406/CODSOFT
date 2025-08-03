import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(text_display.get("1.0", tk.END).strip())
            text_display.delete("1.0", tk.END)
            text_display.insert(tk.END, str(result))
        except Exception:
            text_display.delete("1.0", tk.END)
            text_display.insert(tk.END, "Error")
    elif text == "C":
        text_display.delete("1.0", tk.END)
    else:
        text_display.insert(tk.END, text)
        text_display.see(tk.END)  # auto-scroll to bottom

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Configure root rows/columns
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)
root.columnconfigure(0, weight=1)

# Use Text widget (multiline) instead of Entry
text_display = tk.Text(root, font=("Helvetica", 24), height=2, wrap="none")
text_display.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky="nsew")

# Configure button frame grid for responsiveness
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Buttons layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons
row = 0
col = 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 18), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure button frame rows to expand
for i in range(row + 1):
    button_frame.rowconfigure(i, weight=1)

root.mainloop()
