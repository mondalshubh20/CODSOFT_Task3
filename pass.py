import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_complexity = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(password_complexity) for _ in range(password_length))
    result_label.config(text=f"Generated Password: {password}")

def reset_password():
    length_entry.delete(0, tk.END)
    Us_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator for Codsoft")

# Label & Entry for User id 
label = tk.Label(root, text="User Id")
label.pack()
Us_entry = tk.Entry(root)
Us_entry.pack()

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_password,fg="red")
reset_button.pack()

# Start the GUI application
root.mainloop()
