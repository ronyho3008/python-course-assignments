####

import tkinter as tk
from tkinter import ttk, messagebox

def calculate_dilution():
    try:
        C1 = float(entry_original.get())
        C2 = float(entry_final.get())
        V2 = float(entry_volume.get())
        
        # Convert units for volume
        unit = combo_units.get()
        if unit == "mL":
            V2_ml = V2
        elif unit == "L":
            V2_ml = V2 * 1000
        elif unit == "µL":
            V2_ml = V2 / 1000
        else:
            raise ValueError("Invalid unit")

        # Dilution equation C1V1 = C2V2
        V1_ml = (C2 * V2_ml) / C1
        buffer_ml = V2_ml - V1_ml

        
        message = (
    f"Add:\n"
    f"{V1_ml:.6f} mL of stock solution ({V1_ml*1000:.2f} µL)\n"
    f"{buffer_ml:.6f} mL of buffer ({buffer_ml*1000:.2f} µL)"
)

        messagebox.showinfo("Result", message)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Dilution Calculator")

tk.Label(root, text="original concentration").grid(row=0, column=0)
entry_original = tk.Entry(root)
entry_original.grid(row=0, column=1)

tk.Label(root, text="final concentration").grid(row=1, column=0)
entry_final = tk.Entry(root)
entry_final.grid(row=1, column=1)

tk.Label(root, text="final volume").grid(row=2, column=0)
entry_volume = tk.Entry(root)
entry_volume.grid(row=2, column=1)

tk.Label(root, text="Volume Unit").grid(row=3, column=0)
combo_units = ttk.Combobox(root, values=["mL", "L", "µL"])
combo_units.current(0)
combo_units.grid(row=3, column=1)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_dilution)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
