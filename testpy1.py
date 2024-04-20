import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Create a function to be called when the button is clicked
def button_click():
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Display the current date and time in a message box
    messagebox.showinfo("Current Date and Time", f"The current date and time is: {current_datetime}")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Demo")

# Create a button widget
button = tk.Button(root, text="Click me!", command=button_click)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
