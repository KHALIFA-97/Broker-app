import tkinter as tk
from tkinter import ttk

def generate_system_fields():
    global system_info_entries
    system_number = int(system_number_entry.get())

    for widget in dynamic_fields_frame.winfo_children():
        widget.destroy()

    system_info_entries = []  

    for i in range(system_number):
        label = tk.Label(dynamic_fields_frame, text=f"System {i + 1} Information:")
        label.grid(row=i, column=0, sticky="w")

        entry = tk.Entry(dynamic_fields_frame)
        entry.grid(row=i, column=1)
        
        system_info_entries.append(entry)
    return system_info_entries

def done():
    global system_info
    system_info = []
    for i, entry in enumerate(system_info_entries):
        system_info.append(entry.get())
    root.destroy()
    return system_info

def GoWindow():
    global root
    root = tk.Tk()
    root.title("System Information Input")

    initial_width = 400
    initial_height = 300
    root.geometry(f"{initial_width}x{initial_height}")

    system_number_label = tk.Label(root, text="Enter the number of systems:")
    system_number_label.pack(pady=10)

    global system_number_entry
    system_number_entry = tk.Entry(root)
    system_number_entry.pack(pady=10)

    generate_button = tk.Button(root, text="Generate Fields", command=generate_system_fields)
    generate_button.pack(pady=10)

    global dynamic_fields_frame
    dynamic_fields_frame = tk.Frame(root)
    dynamic_fields_frame.pack(pady=10)

    style = ttk.Style()
    style.configure("Blue.TButton", background="blue", foreground="black")
    done_button = ttk.Button(root, text="Done", style="Blue.TButton", command=done)
    done_button.pack(pady=10)

    root.mainloop()
    return(system_info)

