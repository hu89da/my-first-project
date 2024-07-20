import tkinter as tk
from tkinter import messagebox
import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special symbol."
    if not re.search(r"\d", password):
        return "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    return None

def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(pattern, email):
        return "Email is not valid."
    return None

def submit():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    username_error = validate_username(username)
    password_error = validate_password(password)
    email_error = validate_email(email)

    if username_error:
        messagebox.showerror("Validation Error", username_error)
    elif password_error:
        messagebox.showerror("Validation Error", password_error)
    elif email_error:
        messagebox.showerror("Validation Error", email_error)
    else:
        messagebox.showinfo("Success", "All fields are valid!")

root = tk.Tk()
root.title("User Information")

tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
tk.Label(root, text="Email").grid(row=2)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
email_entry = tk.Entry(root)

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=1)

root.mainloop()
