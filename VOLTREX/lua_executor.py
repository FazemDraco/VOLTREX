import tkinter as tk
from tkinter import ttk, messagebox

# Function to execute Lua code (placeholder)
def execute_lua_code():
    lua_code = textbox.get("1.0", tk.END).strip()
    # Placeholder for actual execution logic
    messagebox.showinfo("Execute", f"Lua Code:\n{lua_code}\n(Execution not implemented)")

# Create the main window
root = tk.Tk()
root.title("Lua Executor")
root.geometry("600x400")  # Set the size of the window
root.configure(bg='#f0f0f0')  # Set background color

# Create a frame for the textbox and button
frame = ttk.Frame(root, padding="20")
frame.pack(expand=True, fill=tk.BOTH)

# Create and place the label
label = ttk.Label(frame, text="Enter Lua Code:", font=("Arial", 14))
label.pack(pady=(0, 10))

# Create and place the textbox
textbox = tk.Text(frame, height=15, width=70, wrap=tk.WORD, font=("Courier New", 12))
textbox.pack(pady=(0, 20))

# Create and place the execute button
execute_button = ttk.Button(frame, text="Execute", command=execute_lua_code)
execute_button.pack()

# Add a version label at the bottom-right corner
version_label = ttk.Label(root, text="Version 1.0", font=("Arial", 10), background='#f0f0f0')
version_label.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Run the application
root.mainloop()
