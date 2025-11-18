import requests
from bs4 import BeautifulSoup
import json
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
def download_page(query):
    """Download search results page from Allrecipes."""
    base_url = "https://www.allrecipes.com/search/results/?search={}"
    url = base_url.format(query.replace(" ", "+"))
    print("URL:", url)  # <-- הדפסת URL לבדיקה
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def extract_recipes(html):
    """Extract recipe data (title, url, rating) from Allrecipes search page."""
    soup = BeautifulSoup(html, "html.parser")
    recipes = []

    # Allrecipes משתמשת בכרטיסי מתכון עם class מסוים
    cards = soup.select("div.card__detailsContainer")  # יתכן ויש צורך לעדכן לפי HTML הנוכחי

    for card in cards:
        title_tag = card.select_one("h3.card__title")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)

        link_tag = card.find("a", class_="card__titleLink")
        href = link_tag["href"] if link_tag else None

        # דירוג — אם קיים
        rating_tag = card.select_one("span.review-star-text")
        rating = None
        if rating_tag:
            text = rating_tag.get_text(strip=True)
            try:
                rating = float(text.split()[1])
            except:
                rating = None

        recipes.append({
            "title": title,
            "url": href,
            "rating": rating
        })

    return recipes

def save_recipes(filename, recipes):
    """Save recipe data to a JSON file."""
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)



