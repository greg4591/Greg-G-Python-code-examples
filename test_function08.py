import pandas as pd # Path: test_function08.py
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

    if not file_path: # If no file was selected
        print("No file selected.")
        return None

    return file_path

file_path = ask_for_excel_file() # Get the file path

def load_excel(file_path): # Load an Excel file into a DataFrame.

    """Load an Excel file into a DataFrame."""

    try:

        return pd.read_excel(file_path)

    except FileNotFoundError:

        print(f"Error: The file at {file_path} was not found.")

        return None

    except Exception as e:

        print(f"Error: {e}")

        return None

df = load_excel(file_path) # Load the Excel file

