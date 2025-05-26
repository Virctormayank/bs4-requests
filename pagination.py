import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com"
url = "/"

# Move this outside the loop to store all quotes from all pages
all_quotes = []

while url:
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "lxml")

    quotes = soup.find_all("div", class_="quote")
    
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        
        # Append a DICTIONARY, not a string
        all_quotes.append({
            "quote": text,
            "author": author
        })

    # Safe next page check
    next_btn = soup.find("li", class_="next")
    if next_btn and next_btn.a:
        url = next_btn.a['href']
    else:
        url = None

# ✅ Total quotes count
print(f"\n✅ Total Quotes Scraped: {len(all_quotes)}")

# ✅ Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print("✅ Quotes saved to 'quotes.csv'")
