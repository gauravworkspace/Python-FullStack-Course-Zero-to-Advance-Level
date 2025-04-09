import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Minimum 8 characters", "red"
    if not any(char.isdigit() for char in password):
        return "Weak: Add a digit", "red"
    if not any(char.isupper() for char in password):
        return "Weak: Add an uppercase letter", "red"
    if not any(char.islower() for char in password):
        return "Weak: Add a lowercase letter", "red"
    if not re.search(r'[!@#$%^&*():;?/><.,|`~]', password):
        return "Medium: Add a special character", "orange"
    return "Strong: Your password is secure", "green"

# Button click function
def check():
    password = entry.get()
    if password.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    result, color = check_password_strength(password)
    result_label.config(text=result, fg=color)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="white")

title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="white")
title.pack(pady=10)

entry_label = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="white")
entry_label.pack()

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=5)

btn = tk.Button(root, text="Check Strength", font=("Arial", 12, "bold"), command=check, bg="#007acc", fg="white")
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="white")
result_label.pack()

root.mainloop()
