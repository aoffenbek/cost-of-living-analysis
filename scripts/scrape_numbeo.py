import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of countries
countries = [
    "Hungary", "Austria", "Slovakia", "Ukraine",
    "Romania", "Serbia", "Croatia", "Slovenia"
]

# Output folder
output_folder = "../data/raw"
os.makedirs(output_folder, exist_ok=True)

# Base URL
BASE_URL = "https://www.numbeo.com/cost-of-living/country_result.jsp?country="

def scrape_country_data(country):
    print(f"Scraping data for {country}...")
    url = BASE_URL + country.replace(" ", "+")
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

    table = soup.find("table", class_="data_wide_table")

    if not table:
        print(f"No table found for {country}")
        return

    rows = []
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) == 3:
            item = cols[0].text.strip()
            price = cols[1].text.strip()
            rows.append((country, item, price))

    df = pd.DataFrame(rows, columns=["Country", "Item", "Price"])
    df.to_csv(f"{output_folder}/{country.lower().replace(' ', '_')}_raw.csv", index=False)

for country in countries:
    scrape_country_data(country)
