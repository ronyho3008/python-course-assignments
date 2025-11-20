# logic.py
import requests
import json

BASE_URL = "https://rest.uniprot.org/uniprotkb/"

def download_uniprot_entry(entry_id: str, output_file: str):
    """
    Downloads a UniProt entry by ID and saves the JSON to a file.
    """
    url = f"{BASE_URL}{entry_id}.json"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Failed to download entry {entry_id}: HTTP {response.status_code}")

    data = response.json()

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return output_file

