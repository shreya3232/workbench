import pandas as pd
import sqlite3
# Load the Excel file into a pandas DataFrame
excel_file = "Credit_Note.xlsx"
data_frame = pd.read_excel(excel_file)

# Convert DataFrame to an SQL file
table_name = "credit_note"
sql_file = "Credit_Note1.sql"

# table_schema = ", ".join([f"{col_name} TEXT" for col_name in data_frame.columns])
# table_creation_statement = f"CREATE TABLE {table_name} ({table_schema});"

# # Generate the SQL insert statements
# insert_statements = []
# for _, row in data_frame.iterrows():
#     values = ", ".join([f"'{str(value)}'" for value in row.values])
#     insert_statements.append(f"INSERT INTO {table_name} VALUES ({values});")

# # Save the SQL file with table creation statement and insert statements
# with open(sql_file, "w") as file:
#     file.write(table_creation_statement + "\n")
#     file.write("\n".join(insert_statements))

# print(f"Conversion completed successfully! SQL file saved as {sql_file}")
columns = []
for column in data_frame.columns:
    column_name = column.replace(" ", "_").lower()
    columns.append(column_name)

create_table_statement = "CREATE TABLE {} (\n    {}\n);\n\n".format(table_name, ",\n    ".join(columns))

# Generate the SQL insert statements
insert_statements = []
for index, row in data_frame.iterrows():
    values = ", ".join([f"'{str(value)}'" for value in row.values])
    insert_statements.append("INSERT INTO {} VALUES ({});".format(table_name, values))

# Save the SQL file with table creation statement and insert statements
with open(sql_file, "w") as file:
    file.write(create_table_statement)
    file.write("\n".join(insert_statements))

print(f"Conversion completed successfully! SQL file saved as {sql_file}")