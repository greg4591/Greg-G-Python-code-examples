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

# Read a specific location (R,C)
def display_specific_location(df, row, column):
    """Display a specific location (R,C) in the DataFrame."""
    print(df.iloc[row, column])

# Filter the data based on a condition
def filter_data(df, condition):
    """Filter the DataFrame based on a condition."""
    filtered_df = df[condition]
    return filtered_df

# Display column J and column B where column B < 1
def display_filtered_columns(df, column_b, column_j):
    """Display specific columns based on a condition."""
    filtered_df = df[df[column_b] < 1]
    print(filtered_df[[column_j, column_b]])

# Filter the data based on column B > 0, column D, and column L
def filter_multiple_columns(df, conditions, columns):
    """Filter the DataFrame based on multiple conditions and display specific columns."""
    filtered_df = df.loc[conditions, columns]
    print(filtered_df)

# Filter the data based on a condition
def filter_specific_columns(df, conditions, columns):
    """Filter the DataFrame based on specific columns and display the results."""
    if all(col in df.columns for col in columns):
        filtered_columns_df = df.loc[conditions, columns]
        print(filtered_columns_df)
    else:
        print("One or more columns do not exist in the DataFrame.")

# Main function to execute the code
def main():
    if os.path.exists(file_path):
        df_xls = load_excel(file_path)
        display_specific_location(df_xls, 4, 4)
        
        # Filter the data based on a condition
        condition = (df_xls.iloc[:, 1] > 0) & (df_xls.iloc[:, 3].notnull()) & (df_xls.iloc[:, 11].notnull())
        columns = df_xls.columns[[1, 3, 11]]
        filter_multiple_columns(df_xls, condition, columns)
        
        # Filter the data based on a condition
        condition = (df_xls['survived'] > 0) & (df_xls['age'] > 18)
        columns = ['survived', 'age']
        filter_specific_columns(df_xls, condition, columns)

if __name__ == "__main__":
    main()

