# mysqltest003.py
# This script is designed to create a SQLite database and perform basic operations.
# It includes functions to create a connection, create a table, insert data, and query data.
import sqlite3
import sys

def create_connection(mytestsqldb):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(mytestsqldb)
        print(f"Connected to database: {mytestsqldb}")
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

def insert_data(conn, name, age):
    """Insert data into the table."""
    try:
        sql_insert_data = """INSERT INTO mytest (name, age) VALUES (?, ?);"""
        cursor = conn.cursor()
        cursor.execute(sql_insert_data, (name, age))
        conn.commit()
        print(f"Inserted data: {name}, {age}")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
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
            print(row)
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")
        sys.exit(1)

def main():
    mytestsqldb = "mytest.db"
    
    # Create a database connection
    conn = create_connection(mytestsqldb)
    
    # Create a table
    create_table(conn)
    
    # Insert some data
    insert_data(conn, "Alice", 30)
    insert_data(conn, "Bob", 25)
    
    # Query the data
    query_data(conn)
    
    # Close the connection
    if conn:
        conn.close()
        print("Connection closed.")
if __name__ == '__main__':
    main()
# End of mysqltest003.py
# This script can be run directly to create a SQLite database, create a table, insert data, and query the data.