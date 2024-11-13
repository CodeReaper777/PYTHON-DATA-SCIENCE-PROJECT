import yfinance as yf

# Download Tesla stock data
tesla_data = yf.download("TSLA", start="2020-01-01", end="2023-01-01")  # Adjust dates as needed
print(tesla_data.head())  # Check the output
