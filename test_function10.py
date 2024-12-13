
import pandas as pd
import numpy as np
import os

file_path  = 'D:\\Python\\Python Test Code\\Financials Sample Data.xlsx'
def load_excel(file_path):
    """Load an Excel file into a DataFrame."""
    return pd.read_excel(file_path)

def display_column(df, column_name):
    """Display a specific column from the DataFrame."""
    print(df[column_name] == "Account" + "Jun")

def display_multiple_columns(df, columns, rows=352):
    """Display specific columns from the DataFrame."""
    print(df[columns].head(rows))

def process_data(df_xls):
    """Process and display specific parts of the DataFrame."""
    # Filter the DataFrame to only include rows where the "Account" column is "Marketing Expense" and "Jun" column is "Jun"
    filtered_df = df_xls.loc[(df_xls['Account'] == "Marketing Expense") & (df_xls['Jun'] == "Jun")]
    
    # Print the filtered DataFrame
    print(filtered_df)

def main():
    #file_path = 'D:\Python\Python Test Code\titanic.xlsx'  # Define the correct file path here
    if os.path.exists(file_path):
        df_xls = load_excel(file_path)
        process_data(df_xls)
        display_multiple_columns(df_xls, ['Account', 'Jun'])
    else:
        print(f"File {file_path} not found.")

if __name__ == "__main__":
    main()
