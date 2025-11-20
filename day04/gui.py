import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import pandas as pd

BASE_URL_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
BASE_URL_ENTRY = "https://rest.uniprot.org/uniprotkb/"

# אחסון תוצאות
results_list = []

# ---------------- פונקציות -----------------
def search_proteins():
    global results_list
    results_list = []  # איפוס תוצאות
    query_text = entry_query.get().strip()
    
    if not query_text:
        messagebox.showerror("Error", "Please enter protein name(s) or Uniprot ID(s).")
        return

    # חיפוש מרובה: מפריד בקומות או רווחים
    queries = [q.strip() for q in query_text.replace(",", " ").split()]
    
    text_results.config(state="normal")
    text_results.delete("1.0", tk.END)
    
    for q in queries:
        try:
            url = f"{BASE_URL_SEARCH}?query={q}&format=json&size=1"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("results"):
                text_results.insert(tk.END, f"No results for: {q}\n\n")
                continue
            
            protein = data["results"][0]
            
            protein_id = protein["primaryAccession"]
            protein_name = protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
            organism = protein["organism"]["scientificName"]
            length = protein["sequence"]["length"]
            
            # שמירה לרשימה
            results_list.append({
                "Query": q,
                "Protein Name": protein_name,
                "Uniprot ID": protein_id,
                "Organism": organism,
                "Length": length
            })
            
            # הצגת מידע
            text_results.insert(tk.END, f"Query: {q}\n")
            text_results.insert(tk.END, f"Protein Name: {protein_name}\n")
            text_results.insert(tk.END, f"Uniprot ID: {protein_id}\n")
            text_results.insert(tk.END, f"Organism: {organism}\n")
            text_results.insert(tk.END, f"Length: {length} aa\n")
            text_results.insert(tk.END, "-"*40 + "\n")
            
        except Exception as e:
            text_results.insert(tk.END, f"Error for {q}: {e}\n")
    
    text_results.config(state="disabled")

def download_fasta():
    if not results_list:
        messagebox.showerror("Error", "No proteins to download. Perform a search first.")
        return
    
    save_path = filedialog.askdirectory(title="Select folder to save FASTA files")
    if not save_path:
        return
    
    for protein in results_list:
        prot_id = protein["Uniprot ID"]
        url = f"{BASE_URL_ENTRY}{prot_id}.fasta"
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_path = f"{save_path}/{prot_id}.fasta"
            with open(file_path, "w") as f:
                f.write(response.text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download {prot_id}: {e}")
    
    messagebox.showinfo("Done", "FASTA files downloaded successfully!")

def save_to_excel():
    if not results_list:
        messagebox.showerror("Error", "No data to save. Perform a search first.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files","*.xlsx")])
    if not file_path:
        return
    
    df = pd.DataFrame(results_list)
    df.to_excel(file_path, index=False)
    messagebox.showinfo("Saved", f"Results saved to {file_path}")

# ---------------- GUI -----------------
root = tk.Tk()
root.title("UniProt Protein Finder")
root.geometry("600x500")

tk.Label(root, text="Enter protein name(s) or Uniprot ID(s) (separate multiple with space or comma):").pack(pady=5)
entry_query = tk.Entry(root, width=60)
entry_query.pack(pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_search = tk.Button(frame_buttons, text="Search", command=search_proteins)
btn_search.grid(row=0, column=0, padx=5)

btn_fasta = tk.Button(frame_buttons, text="Download FASTA", command=download_fasta)
btn_fasta.grid(row=0, column=1, padx=5)

btn_excel = tk.Button(frame_buttons, text="Save to Excel", command=save_to_excel)
btn_excel.grid(row=0, column=2, padx=5)

tk.Label(root, text="Results:").pack(pady=5)

text_results = tk.Text(root, width=70, height=20, state="disabled")
text_results.pack(pady=5)

root.mainloop()
