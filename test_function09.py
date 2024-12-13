import pandas as pd # Path: test_function09.py
import numpy as np  # Compare this snippet from test_function05.py:
import os # import pandas as pd
import glob # 
import tkinter as tk #  Sample data
from tkinter import filedialog # data = { 'Department': ['HR', 'IT', 'Finance ']}

def ask_for_excel_file(): # Ask the user to select an Excel file

    root = tk.Tk() # Create the root window
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(
        initialdir="D:/Python/Python Test Code/",
        title="Select an Excel file",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    ) # Ask the user to select an Excel file

def create_blank_excel(file_path):
    """Create a blank Excel spreadsheet."""
    try:
        # Create a new DataFrame
        df = pd.DataFrame()
        
        # Save the DataFrame to an Excel file
        df.to_excel(file_path, index=False)
        
        print(f"Blank Excel file created at {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Define the path for the new blank Excel file
new_file_path = "D:/Python/Python Test Code/test_spreadsheet.xlsx"

# Create the blank Excel file
create_blank_excel(new_file_path) 

