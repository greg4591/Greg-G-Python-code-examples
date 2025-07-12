# Open northwind database
# This script connects to the Northwind database and retrieves some data.   
# It requires the `sqlite3` module to be installed.
import sqlite3
import sys
import json

con = sqlite3.connect('northwind.db')
cur = con.cursor()
# Fetching data from the Customers table
cur.execute("SELECT * FROM Customers")
rows = cur.fetchall()
# Convert the rows to a list of dictionaries
customers = []
for row in rows:
    customers.append({
        'CustomerID': row[0],
        'CompanyName': row[1],
        'ContactName': row[2],
        'ContactTitle': row[3],
        'Address': row[4],
        'City': row[5],
        'Region': row[6],
        'PostalCode': row[7],
        'Country': row[8],
        'Phone': row[9],
        'Fax': row[10]
    })
# Convert the list of dictionaries to JSON
json_data = json.dumps(customers, indent=4)
# Print the JSON data to stdout
print(json_data)
# Close the database connection
con.close()
# Exit the script
sys.exit(0)
# End of script
