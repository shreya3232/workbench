import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = 'https://www.indianyellowpages.com/directory/e-learning-solution.htm'

# Send a GET request to the URL
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Extract titles
title_elements = soup.select('.name')
titles = [title.text.strip() for title in title_elements]

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Title': titles})

# Save the DataFrame to an Excel file
df.to_excel('scraped_data1.xlsx', index=False)
