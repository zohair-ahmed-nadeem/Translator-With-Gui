# Import the necessary modules
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("ComboBox Example")
root.geometry("300x200")

# Create a label to display the selected item
selected_label = tk.Label(root, text="Selected Item: None")
selected_label.pack(pady=10)

# Function to update the label when an item is selected
def update_label(event):
    selected_item = combo.get()
    selected_label.config(text=f"Selected Item: {selected_item}")

# Create a ComboBox
combo = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3", "Item 4"])
combo.pack(pady=20)

# Bind the ComboBox selection event to the update_label function
combo.bind("<<ComboboxSelected>>", update_label)

# Run the Tkinter event loop
root.mainloop()
