from logic import download_page, extract_recipes, save_recipes

def main():
    print("Allrecipes Recipe Downloader")

    query = input("Enter search term (e.g. 'chicken soup'): ").strip()
    filename = input("Enter output filename (e.g. recipes.json): ").strip()

    print("Downloading data...")
    html = download_page(query)
    recipes = extract_recipes(html)
    save_recipes(filename, recipes)

    print(f"Saved {len(recipes)} recipes to {filename}")

if __name__ == "__main__":
    main()


