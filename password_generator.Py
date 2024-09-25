import random
import tkinter as tk
from tkinter import messagebox


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
           '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to generate the password
def generate_password():
    try:
        n_letters = int(entry_letters.get())
        n_symbols = int(entry_symbols.get())
        n_numbers = int(entry_numbers.get())
        
        password = []
        
        for _ in range(n_letters):
            password.append(random.choice(letters))
            
        for _ in range(n_symbols):
            password.append(random.choice(symbols))
            
        for _ in range(n_numbers):
            password.append(random.choice(numbers))
        
        random.shuffle(password)
        
        # Convert the list to a string
        password_string = "".join(password)
        
        # Display the generated password in the output label
        password_output.config(text=f"Generated Password: {password_string}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for letters, symbols, and numbers.")

# Creating the main window
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# Ensure the grid expands to fill the window
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Title label
title_label = tk.Label(window, text="Welcome to Password Generator", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Label and entry for number of letters
label_letters = tk.Label(window, text="How many letters in your password?")
label_letters.grid(row=1, column=0, pady=5, sticky="e")
entry_letters = tk.Entry(window)
entry_letters.grid(row=1, column=1, pady=5, sticky="w")

# Label and entry for number of symbols
label_symbols = tk.Label(window, text="How many symbols in your password?")
label_symbols.grid(row=2, column=0, pady=5, sticky="e")
entry_symbols = tk.Entry(window)
entry_symbols.grid(row=2, column=1, pady=5, sticky="w")

# Label and entry for number of numbers
label_numbers = tk.Label(window, text="How many numbers in your password?")
label_numbers.grid(row=3, column=0, pady=5, sticky="e")
entry_numbers = tk.Entry(window)
entry_numbers.grid(row=3, column=1, pady=5, sticky="w")

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

# Label to display the generated password
password_output = tk.Label(window, text="", font=("Arial", 12))
password_output.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

# Start the GUI event loop
window.mainloop()
