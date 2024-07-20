import tkinter as tk
from tkinter import simpledialog, messagebox

def display_right_angle_triangle():
    n = simpledialog.askinteger("Input", "Enter the number of rows for the right-angle triangle:")
    if n is not None:
        result = ""
        for i in range(1, n+1):
            result += "1" * i + "\n"
        messagebox.showinfo("Right-Angle Triangle", result)

def display_palindromic_triangle():
    n = simpledialog.askinteger("Input", "Enter the number of rows for the palindromic triangle:")
    if n is not None:
        result = ""
        for i in range(1, n+1):
            result += " " * (n - i) + ''.join(str(x) for x in range(1, i)) + ''.join(str(x) for x in range(i, 0, -1)) + "\n"
        messagebox.showinfo("Palindromic Triangle", result)

def show_help():
    help_text = (
        "1. Display a right-angle Triangle ones: Prompts for the number of rows and displays a right-angle triangle with '1's.\n"
        "2. Display a Palindromic Triangle: Prompts for the number of rows and displays a palindromic triangle.\n"
        "3. Help: Displays this help message.\n"
        "4. Exit: Exits the application."
    )
    messagebox.showinfo("Help", help_text)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Menu")

tk.Label(root, text="Menu").pack(pady=10)

tk.Button(root, text="1. Display a right-angle Triangle ones", command=display_right_angle_triangle).pack(pady=5)
tk.Button(root, text="2. Display a Palindromic Triangle", command=display_palindromic_triangle).pack(pady=5)
tk.Button(root, text="3. Help", command=show_help).pack(pady=5)
tk.Button(root, text="4. Exit", command=exit_program).pack(pady=5)

root.mainloop()