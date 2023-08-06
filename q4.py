import tkinter as tk

def calculate_cache_mapping():
    # Get user inputs from the GUI
    cache_size_kb = int(cache_size_entry.get())
    block_size_b = int(block_size_entry.get())
    memory_address = int(memory_address_entry.get(), 16)  # Assuming hex input, convert to int

    # Calculate cache parameters
    num_cache_lines = cache_size_kb * 1024 // block_size_b
    tag_bits = 32 - (block_size_b.bit_length() + num_cache_lines.bit_length()).bit_length()
    block_offset_bits = block_size_b.bit_length().bit_length()

    # Perform cache mapping calculations
    cache_line = (memory_address >> block_offset_bits) % num_cache_lines
    tag = memory_address >> (block_offset_bits + num_cache_lines.bit_length())

    # Display the results in the GUI
    cache_line_label.config(text=f"Cache Line: {cache_line}")
    tag_bits_label.config(text=f"Tag Bits: {tag_bits}")
    tag_label.config(text=f"Tag: {hex(tag)}")

# GUI setup
root = tk.Tk()
root.title("Cache Mapping Tool")

cache_size_label = tk.Label(root, text="Cache Size (KB):")
cache_size_label.pack()
cache_size_entry = tk.Entry(root)
cache_size_entry.pack()

block_size_label = tk.Label(root, text="Block Size (B):")
block_size_label.pack()
block_size_entry = tk.Entry(root)
block_size_entry.pack()

memory_address_label = tk.Label(root, text="Memory Address (hex):")
memory_address_label.pack()
memory_address_entry = tk.Entry(root)
memory_address_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_cache_mapping)
calculate_button.pack()

cache_line_label = tk.Label(root, text="Cache Line: ")
cache_line_label.pack()

tag_bits_label = tk.Label(root, text="Tag Bits: ")
tag_bits_label.pack()

tag_label = tk.Label(root, text="Tag: ")
tag_label.pack()

root.mainloop()
