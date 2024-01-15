# Importing libraries and our file of functions 
import tkinter
from tkinter import ttk
from Functions import *

# Creating our window and define its sizes, its title and resizability
root = tkinter.Tk()
root.title("Password Cracker")
root.geometry("380x480")
root.resizable(0,0)

# Create file
initialize_file()

# Style for the labels
style = ttk.Style()
style.configure("TLabel", font=("Agency FB", 18), padding=(10, 5))

# Creating header
header_label = ttk.Label(root, text="Let us crack your password")
header_label.pack(padx=10, pady=10)
header_label.grid(row=0, column=0, padx=10, pady=10)

# Create the password entry field
password_entry = ttk.Entry(root, show="")
password_entry.grid(row=1, column=0, padx=10, pady=10)

# Create the crack button
crack_button = ttk.Button(root, text="Crack Password", command=lambda: crack_password(root, cracked_password_label, password_entry.get()))
crack_button.grid(row=2, column=0, padx=10, pady=10)

# Create the label that will display the cracked password, the number of attempts, time spent, and password strength
cracked_password_label = ttk.Label(root, text="", wraplength=200)
cracked_password_label.grid(row=3, column=0, padx=10, pady=10)

# Start our tkinter program
root.mainloop()