import requests
from bs4 import BeautifulSoup

# Replace with the actual URL of Tesla's financials page on Yahoo Finance
url = "https://finance.yahoo.com/quote/TSLA/financials"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate and extract revenue data
# Find the table with financial data; this depends on the structure of the page
# You will need to adjust this part based on the actual HTML structure of the page
revenue_data = []

# This is a placeholder for finding the revenue data from the table; you'll need to inspect the page
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if columns and "Total Revenue" in columns[0].text:
        revenue_data.append(columns[1].text)  # Assuming the revenue is in the second column

print(revenue_data)
