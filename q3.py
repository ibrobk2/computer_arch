import tkinter as tk

def on_submit():
    selected_policy = var.get()
    print("Selected Policy:", selected_policy)

root = tk.Tk()
root.title("Cache Write Policy Selection")

# Create a variable to hold the selected policy
var = tk.StringVar()

# Create radio buttons for write-back and write-through options
tk.Radiobutton(root, text="Write-Back", variable=var, value="Write-Back").pack(anchor=tk.W)
tk.Radiobutton(root, text="Write-Through", variable=var, value="Write-Through").pack(anchor=tk.W)

# Submit button
tk.Button(root, text="Submit", command=on_submit).pack()

root.mainloop()
