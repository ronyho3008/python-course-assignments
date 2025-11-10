import tkinter as tk
from tkinter import ttk, messagebox
from dilution_logic import calculate_dilution

def run_calculator():
    try:
        C1 = float(entry_original.get())
        C2 = float(entry_final.get())
        V2 = float(entry_volume.get())

        unit = combo_units.get()
        if unit == "L":
            V2 *= 1000
        elif unit == "µL":
            V2 /= 1000

        V1, buffer = calculate_dilution(C1, C2, V2)
        msg = f"Add:\n{V1:.3f} mL stock ({V1*1000:.1f} µL)\n{buffer:.3f} mL buffer"
        messagebox.showinfo("Result", msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Dilution Calculator")

tk.Label(root, text="Original concentration").grid(row=0, column=0)
entry_original = tk.Entry(root)
entry_original.grid(row=0, column=1)

tk.Label(root, text="Final concentration").grid(row=1, column=0)
entry_final = tk.Entry(root)
entry_final.grid(row=1, column=1)

tk.Label(root, text="Final volume").grid(row=2, column=0)
entry_volume = tk.Entry(root)
entry_volume.grid(row=2, column=1)

tk.Label(root, text="Unit").grid(row=3, column=0)
combo_units = ttk.Combobox(root, values=["mL", "L", "µL"])
combo_units.current(0)
combo_units.grid(row=3, column=1)

tk.Button(root, text="Calculate", command=run_calculator).grid(row=4, column=0, columnspan=2)

root.mainloop()
