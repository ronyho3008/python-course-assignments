# main.py
from logic import download_uniprot_entry

def main():
    print("UniProt Protein Downloader")
    print("---------------------------")

    protein_id = input("Enter a UniProt ID (e.g. P68871): ").strip()
    filename = f"{protein_id}.json"

    try:
        download_uniprot_entry(protein_id, filename)
        print(f"Download complete! Saved as '{filename}'")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

