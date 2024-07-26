import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

# Function to execute Lua code (placeholder)
def execute_lua_code():
    lua_code = textbox.get("1.0", tk.END).strip()
    # Placeholder for actual execution logic
    messagebox.showinfo("Execute", f"Lua Code:\n{lua_code}\n(Execution not implemented)")

# Create the main window
root = tk.Tk()
root.title("Lua Executor")
root.geometry("700x500")  # Adjusted size for a more spacious layout
root.configure(bg='#2e2e2e')  # Dark background color

# Create a frame for the main content
main_frame = ttk.Frame(root, padding="20", style="TFrame")
main_frame.pack(expand=True, fill=tk.BOTH)

# Configure styles
style = ttk.Style()
style.configure("TFrame", background="#2e2e2e")
style.configure("TLabel", background="#2e2e2e", foreground="white", font=("Arial", 14))
style.configure("TButton", padding=6, relief="flat", background="#4a4a4a", foreground="white", font=("Arial", 12))
style.map("TButton", background=[("active", "#5a5a5a")])

# Create and place the label
label = ttk.Label(main_frame, text="Enter Lua Code:")
label.pack(pady=(0, 10))

# Create and place the textbox with scrolling
textbox = ScrolledText(main_frame, height=20, width=80, wrap=tk.WORD, font=("Courier New", 12))
textbox.pack(pady=(0, 20))

# Create and place the execute button
execute_button = ttk.Button(main_frame, text="Execute", command=execute_lua_code)
execute_button.pack()

# Add a version label at the bottom-right corner
version_label = ttk.Label(root, text="Version 1.0", font=("Arial", 10), background='#2e2e2e', foreground="white")
version_label.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Run the application
root.mainloop()
