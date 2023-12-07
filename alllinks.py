import csv
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

# List of Amazon links
amazon_links = [
    'https://www.amazon.in/GOVO-GOSURROUND-900-Subwoofer-Bluetooth/dp/B09YV5LC7F/ref=sr_1_3?keywords=govo+soundbar&qid=1685081351&sprefix=govo%2Caps%2C696&sr=8-3',
        'https://www.amazon.in/dp/B09YV5LC7F?th=1',
        'https://amazon.in/dp/B09P33L9ZR',
        'https://amazon.in/dp/B09P32F8M5',
        'https://amazon.in/dp/B0B2DZZ4ZZ',
        'https://amazon.in/dp/B09P37YKMS',
        'https://www.amazon.in/dp/B09P31MBGH',
]

# List of Flipkart links
flipkart_links = [
    "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVZYZYFHXD",
    "https://www.flipkart.com/product/p/itme?pid=ACCGBWGV4ENPNSXH",
    "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPZHHZQFAM",
    "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPSCA9WYFU",	
    "https://www.flipkart.com/product/p/itme?pid=ACCGGWZPQE7YFRGC",	
    "https://www.flipkart.com/product/p/itme?pid=ACCGGWZP9QZNUDAG",	
    "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVUJRBZWDN",	
    "https://www.flipkart.com/product/p/itme?pid=ACCGBWGVRFGFGZZP",	
]

# List of govo.life links
govolife_links = [
    'https://govo.life/products/gobuds-600-earbuds',
    'https://govo.life/products/gobuds-902-earbuds',
    'https://govo.life/products/gobuds-400-earbuds',
    'https://govo.life/products/gobuds-920-earbuds',
    'https://govo.life/products/gobuds-621-earbuds',
    'https://govo.life/products/gobuds-901-earbuds',
    'https://govo.life/products/gobuds-410-earbuds',
]

# Function to scrape data and return a list of dictionaries
def scrape_amazon_data(links):
    scraped_data = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('span', {'id': 'productTitle'})
        price = soup.find('span', {'class': 'a-offscreen'})
        if title and price:
            title = title.text.strip()
            price = price.text.strip()
            scraped_data.append({'Website': 'Amazon', 'Title': title, 'Price': price})
    return scraped_data


# Function to scrape Flipkart data
def scrape_flipkart_data(links):
    scraped_data = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('div', {'class': 'B_NuCI'})
        price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
        if title and price:
            title = title.text.strip()
            price = price.text.strip()
            scraped_data.append({'Website': 'Flipkart', 'Title': title, 'Price': price})
    return scraped_data

# Function to scrape govo.life data
def scrape_govolife_data(links):
    scraped_data = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'class': 'font-semibold'})
        price = soup.find('span', {'class': 'font-semibold product-selling-price text-primary me-2 me-lg-12'})
        if title and price:
            title = title.text.strip()
            price = price.text.strip()
            scraped_data.append({'Website': 'govolife', 'Title': title, 'Price': price})
        
    return scraped_data
amazon_data = scrape_amazon_data(amazon_links)
flipkart_data = scrape_flipkart_data(flipkart_links)
govolife_data = scrape_govolife_data(govolife_links)

# Combine all scraped data
all_data = amazon_data + flipkart_data + govolife_data

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Website', 'Title', 'Price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)

print("Scraped data has been saved to scraped_data.csv")
