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

def main():
    file_path = 'titanic3.xlsx'
    df_xls = load_excel(file_path)
    
    display_headers(df_xls)
    display_column(df_xls, 'name')
    display_multiple_columns(df_xls, ['name', 'age', 'cabin'])
    #display_multiple_columns(df_xls, ['survived', 'name', 'sex', 'age'], rows=3)

if __name__ == "__main__":
    main()
 
