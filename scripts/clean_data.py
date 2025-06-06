import os
import pandas as pd
import re

input_folder = "../data/raw"
output_folder = "../data/cleaned"
os.makedirs(output_folder, exist_ok=True)

def clean_price(value):
    try:
        value = re.sub(r"[^\d,.-]", "", value)
        value = value.replace(",", "")
        return float(value)
    except:
        return None

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(input_folder, filename))
        df["Price_Clean"] = df["Price"].apply(clean_price)
        df.to_csv(os.path.join(output_folder, filename.replace("_raw", "")), index=False)
