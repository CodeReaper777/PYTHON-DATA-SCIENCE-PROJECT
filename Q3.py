# Download GameStop stock data
gamestop_data = yf.download("GME", start="2020-01-01", end="2023-01-01")  # Adjust dates as needed
print(gamestop_data.head())
