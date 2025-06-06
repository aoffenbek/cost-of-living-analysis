# Cost of Living Comparison: Central Europe

This project scrapes and analyzes cost of living data from Numbeo for Hungary and its neighboring countries (Austria, Slovakia, Romania, Ukraine, Serbia, Croatia, Slovenia).

## Features

- Web scraping with BeautifulSoup
- Data cleaning with Pandas
- Exploratory analysis (e.g. rent, groceries)
- Extendable to more countries or currencies

## How to Run

1. Clone the repo
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Scrape data:
   ```bash
   python scripts/scrape_numbeo.py
   ```
4. Clean data:
   ```bash
   python scripts/clean_data.py
   ```
5. Explore data using Jupyter Notebook

# 📊 Power BI Dashboard

This folder contains:
- `cost_of_living_all_countries.csv`: Cleaned cost of living data for Hungary and neighboring countries
- `CostOfLivingDashboard.pbix`: Power BI dashboard file

## Features:
- Compare rent, groceries, restaurant prices
- Filter by country or item
- Easy-to-read charts and matrix tables

## How to Use
1. Open `CostOfLivingDashboard.pbix` in Power BI Desktop
2. Refresh data from the CSV if needed
3. Explore cost comparisons across Central Europe
