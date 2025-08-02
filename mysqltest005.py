import sqlite3
import sys

def create_connection(mytestsql005db):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(mytestsql005db)
        print("Connection to SQLite DB successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
    return conn

def create_table(conn):
    """Create a table in the SQLite database."""
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS mytest (
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  name TEXT NOT NULL,
                                  age INTEGER
                              );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        sys.exit(1)

def ask_for_input(prompt):
    """Ask the user for input and return it."""
    return input(prompt + " ")

def insert_data(conn, name, age):
    """Insert data into the table."""
    sql_insert_data = """INSERT INTO mytest (name, age) VALUES (?, ?);"""
    cursor = conn.cursor()
        #cursor.execute(sql_insert_data, (name, age))
    if name and age is not None:
        cursor.execute(sql_insert_data, (name, age))
        conn.commit()
        print(f"Inserted data: {name}, {age}")
        print("Name and age have been entered successfully.")
    else:
        print("Name and age were not entered successfully.")
        sys.exit(1)

def query_data(conn):
    """Query data from the table."""
    try:
        sql_query_data = """SELECT * FROM mytest;"""
        cursor = conn.cursor()
        cursor.execute(sql_query_data)
        rows = cursor.fetchall()
        print("Query results:")
        for row in rows:
            if row:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")
        sys.exit(1)

# Optionally, remove data by ID
# id_number = input("Enter the ID of the record to remove: ")
# remove_data_by_id(conn, id_number)
def Remove_data_by_ID(conn, id_number):
    """Remove data from the table by selected ID number."""
    try:
        sql_delete_data = """DELETE FROM mytest WHERE id = ?;"""
        cursor = conn.cursor()
        cursor.execute(sql_delete_data, (id_number,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Record with ID {id_number} removed successfully.")
        else:
            print(f"No record found with ID {id_number}.")
    except sqlite3.Error as e:
            print(f"Error removing data: {e}")
            sys.exit(1)
    

def main():
    mytestsqldb = "mytest.db"
    
    # Create a database connection
    conn = create_connection(mytestsqldb)
    
    # Create table
    create_table(conn)
    
    # Ask for user input and insert data
    name = input("What is your name? ")
    age = input("What is your age? ")
    
    # Insert data into the table
    insert_data(conn, name, age)
    
    # Query the data
    query_data(conn)

    # Optionally, remove data by ID
    Remove_data_by_ID(conn, id_number)
    id_number = input("Enter the ID of the record to remove: ")

    # If the connection exists, close it
    # Close the connection
    if conn:
        conn.close()
        print("Connection to SQLite DB closed.")

# Run the main function if this script is executed
mytestsql005db = "mytest.db" # Define the database name
conn = create_connection(mytestsql005db) # Create a database connection
create_table(conn) # Create the table
name = ask_for_input("What is your name? ") # Ask for the person's name
age = ask_for_input("What is your age? ") # Ask for the person's age
    
insert_data(conn, name, age) # Insert the data into the table
    
query_data(conn) # Query the data from the table

Remove_data_by_ID(conn, input("Enter the ID of the record to remove: ")) # Remove data by ID
    # Close the connection
    
if conn: # Close the connection if it exists
        conn.close()
        print("Connection to SQLite DB closed.")