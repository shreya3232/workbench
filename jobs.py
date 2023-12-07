# # import requests
# # from bs4 import BeautifulSoup
# # import re
# # import pandas as pd

# # # List of URLs to scrape
# # urls = [
# #     'http://yellowpages.in/b/white-house-apparels-pvt-ltd-himayat-nagar-hyderabad/869060096',
# #     'http://yellowpages.in/b/sri-krishna-electricals-troop-bazar-hyderabad/703722148',
# #     'http://yellowpages.in/b/central-book-point-nanal-nagar-hyderabad/473543359'
# #     # Add more URLs here
# # ]

# # # Initialize empty lists to store the extracted data
# # data = []

# # # Scrape data from each URL
# # for url in urls:
# #     response = requests.get(url)
# #     soup = BeautifulSoup(response.content, 'html.parser')

# #     email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
# #     email_addresses = set(re.findall(email_pattern, soup.get_text()))

# #     phone_pattern = re.compile(r'(\+\d{1,2}\s?)?(\d{3}\s?){2}\d{4}')
# #     phone_numbers = set(re.findall(phone_pattern, soup.get_text()))

# #     business_name = soup.select_one('.businessTitle').text.strip()

# #     # Format phone numbers and remove non-digit characters
# #     formatted_phone_numbers = [re.sub(r'\D', '', number) for number in phone_numbers]

# #     # Append the extracted data as a dictionary
# #     data.append({
# #         'Business Name': business_name,
# #         'Email Addresses': (email_addresses),
# #         'Phone Numbers': ', '.join(formatted_phone_numbers)
# #     })

# # # Create a DataFrame from the extracted data
# # df = pd.DataFrame(data)

# # # Save the DataFrame to an Excel file
# # df.to_excel('scraped_data.xlsx', index=False)
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # List of URLs to scrape
# urls = [
#     # 'http://yellowpages.in/b/white-house-apparels-pvt-ltd-himayat-nagar-hyderabad/869060096',
#     # 'http://yellowpages.in/b/sri-krishna-electricals-troop-bazar-hyderabad/703722148',
#     # 'http://yellowpages.in/b/central-book-point-nanal-nagar-hyderabad/473543359'
#     'http://yellowpages.in/hyderabad/sarees-and-blouses/380244742'
#     # Add more URLs here
# ]

# # Initialize empty lists to store the extracted data
# data = []

# # Scrape data from each URL
# for url in urls:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract business name
#     business_name_element = soup.select_one('.eachPopularTitle.hasOtherInfo')
#     business_name = business_name_element.text.strip() if business_name_element else ''

#     # Extract email addresses
#     # email_elements = soup.select('#MainContent_divEmail')
#     # email_addresses = [email.text.strip() for email in email_elements]

#     # Extract phone numbers
#     phone_elements = soup.select('.businessContact')
#     phone_numbers = [phone.text.strip() for phone in phone_elements]

#     # Append the extracted data as a dictionary
#     data.append({
#         'Business Name': business_name,
#         # 'Email Addresses': ', '.join(email_addresses),
#         'Phone Numbers': ', '.join(phone_numbers)
#     })

# # Create a DataFrame from the extracted data
# df = pd.DataFrame(data)

# # Save the DataFrame to an Excel file
# df.to_excel('scraped_data.xlsx', index=False)
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL to scrape
url = 'http://yellowpages.in/hyderabad/sarees-and-blouses/380244742'

# Send a GET request to the URL
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Extract website title
title_element = soup.select_one('.websiteLink')
website_title = title_element.get('title') if title_element else ''

# Extract phone numbers
phone_pattern = re.compile(r'(\+\d{1,2}\s?)?(\d{3}\s?){2}\d{4}')
phone_numbers = set(re.findall(phone_pattern, soup.get_text()))

# Format phone numbers and remove non-digit characters
formatted_phone_numbers = [re.sub(r'\D', '', number[0]) for number in phone_numbers]

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'Website Title': [website_title],
    'Phone Numbers': [', '.join(formatted_phone_numbers)]
})

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
