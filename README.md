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

## Next Steps

- Create a Streamlit or Power BI dashboard
- Normalize by local income
- Add time-based tracking
