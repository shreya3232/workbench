import mysql.connector
import requests

# Set up the MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shreyas@444",
  database="daily_data"
)

# Define the number of columns
num_columns = 5  # Change this to the actual number of columns in your Amazon Ads data

# Retrieve the data from Amazon Ads
url = "https://advertising.amazon.in/cm/campaigns?entityId=ENTITY1Z3JTO90W3H5D"
response = requests.get(url)
data = response.json()

# Insert the data into MySQL
cursor = mydb.cursor()
for row in data:
    values = tuple(row.values()[:num_columns])
    # Assuming you have a table named 'amazon_ads_data' with the corresponding number of columns
    # Modify the following SQL statement to match your table structure
    sql = "INSERT INTO amazon_ads_data VALUES ({})".format(", ".join(["%s"] * num_columns))
    cursor.execute(sql, values)

mydb.commit()
