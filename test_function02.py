# The code in the test_function.py file is a refactored version of the code snippet from Test_Excel_worksheet-01.py.
# The code has been organized into functions, making it more modular and reusable.
# The main function is used to call the other functions and execute the code.
# By organizing the code into functions, it becomes easier to read, maintain, and test.
# The functions can be reused in other parts of the code or in other scripts.
# The code follows best practices for function naming, documentation, and structure.
# The code is more readable and easier to understand compared to the original snippet.
# The code is more maintainable and extensible, allowing for easier updates and modifications in the future.
# The code can be easily tested by writing unit tests for each function.

import pandas as pd
import numpy as np
import os

file_path  = 'D:\\Python\\Python Test Code\\titanic3.xlsx'
def load_excel(file_path):
    """Load an Excel file into a DataFrame."""
    return pd.read_excel(file_path)

def display_headers(df):
    """Display the column headers of the DataFrame."""
    print(df.columns)

def display_column(df, column_name):
    """Display a specific column from the DataFrame."""
    print(df[column_name])

def display_multiple_columns(df, columns, rows=10):
    """Display specific columns from the DataFrame."""
    print(df[columns][:rows])

def process_data(df_xls):
    """Process and display various parts of the DataFrame."""
    # Read each row
    print(df_xls.head(5))
    print(df_xls.iloc[3:4])
    for index, row in df_xls.iterrows():
        display_specific_row(df_xls, index)

def main():
    #file_path = 'D:\Python\Python Test Code\titanic.xlsx'  # Define the correct file path here
    if os.path.exists(file_path):
        df_xls = load_excel(file_path)
        process_data(df_xls)
    else:
        print(f"File {file_path} not found.")

# Removed duplicate process_data function

def display_specific_row(df, row_index):
    """Display a specific row from the DataFrame."""
    print(df.iloc[row_index:row_index+1])

# Read each row and column
def display_selected_columns(df, columns):
    """Display selected columns from the DataFrame."""
    for index, row in df.iterrows():
        print(index, row[columns].values)

# Read each row and column
def display_rows_with_condition(df, column_name, condition):
    """Display rows where a specific column matches a condition."""
    print(df.loc[df[column_name] == condition])

# Display summary statistics
def display_summary_statistics(df):
    """Display summary statistics of the DataFrame."""
    print(df.describe())


# Display the DataFrame sorted by specific columns
def display_sorted_values(df, columns, ascending=True):
    """Display the DataFrame sorted by specific columns."""
    print(df.sort_values(columns, ascending=ascending))

if __name__ == "__main__":
    main()
