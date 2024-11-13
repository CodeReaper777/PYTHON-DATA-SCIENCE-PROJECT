import requests
from bs4 import BeautifulSoup

# Replace with the actual URL of GameStop's financials page on Yahoo Finance
url = "https://finance.yahoo.com/quote/GME/financials"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing financial data
revenue_data = []

# Loop through the rows to extract revenue information
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if columns and "Total Revenue" in columns[0].text:
        revenue_data.append(columns[1].text)  # Adjust the index if necessary

print(revenue_data)
