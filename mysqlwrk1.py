import pandas as pd
import mysql.connector
# import datetime
# Establish a connection to your MySQL database
cnx = mysql.connector.connect(
    user='u6kn9zefxdjjjdxs',
    password='YpH2dPPhgoZhuwUGYSL',
    # password='jQb8uyyB2f',

    host='bd5ywrh4posn9eoqjfoh-mysql.services.clever-cloud.com',
    database='bd5ywrh4posn9eoqjfoh'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Retrieve the list of Excel files you want to import
import glob

excel_files = glob.glob('result.xlsx')

for file in excel_files:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    # df = df.dropna()
    # df = df.head(1)
    df = df.fillna("")
    df.drop_duplicates()

    if df.empty:
        continue
    
    table_name = 'all_data'  # Adjust the table name

    # Prepare the column names
    columns = ', '.join(['`' + col + '`' for col in df.columns])

    # Prepare the placeholders for the VALUES clause
    placeholders = ', '.join(['%s'] * len(df.columns))

    # Prepare the INSERT statement
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Convert DataFrame to a list of tuples (each tuple representing a row)
    rows = [tuple(row) for row in df.values]

    # Execute the INSERT statement for each row
    cursor.executemany(query, rows)
    cnx.commit()

# Close the cursor and the database connection
cursor.close()
cnx.close()
