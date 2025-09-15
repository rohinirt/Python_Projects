import pandas as pd
import yfinance as yf

# Download last 30 days of Amazon stock data
amazon = yf.download("AMZN", start="2025-01-01", interval="1d")

# Reset index so Date becomes a column
amazon = amazon.reset_index()

# Rename columns manually
amazon.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Format Date column
amazon['Date'] = pd.to_datetime(amazon['Date']).dt.strftime('%Y-%m-%d')

# File path for saving
filename = r"D:\Rohini Personal\Data Analysis\Projects Datasets\Amazon_Automation\amazon_stock.csv"

try:
    existing = pd.read_csv(filename)
    updated = pd.concat([existing, amazon]).drop_duplicates(subset=['Date'])
    updated.to_csv(filename, index=False)
except FileNotFoundError:
    amazon.to_csv(filename, index=False)

print(f"✅ Stock data saved successfully! Latest date: {amazon['Date'].max()}")
