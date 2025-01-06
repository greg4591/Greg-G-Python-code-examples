import pandas as pd
import openpyxl
from openpyxl.chart import LineChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows

# Load the Excel file
file_path = 'Financials Sample Data.xlsx'
df = pd.read_excel(file_path)

# Filter the data for specific accounts for the year 2019
accounts = ['Travel & Entertainment Expense', 'Commissions Expense', 'Consulting Expense', 'Cost of Goods Sold']
filtered_data = df[(df['Account'].isin(accounts)) & (df['Year'] == 2019)]

# Create a new workbook and add the filtered data
new_workbook = openpyxl.Workbook()
sheet = new_workbook.active
sheet.title = 'Expenses 2019'

# Write the filtered data to the new workbook
for row in dataframe_to_rows(filtered_data, index=False, header=True):
    sheet.append(row)

# Create a Line Chart
chart = openpyxl.chart.BarChart()
chart.type = "col"
chart.title = "Expenses 2019"
chart.style = 13
chart.y_axis.title = 'Expense'
chart.x_axis.title = 'Account'

# Reference the data for the chart
data = Reference(sheet, min_col=3, min_row=1, max_col=3, max_row=len(filtered_data) + 1)
categories = Reference(sheet, min_col=2, min_row=2, max_row=len(filtered_data) + 1)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# Add the chart to the sheet
sheet.add_chart(chart, "E5")

# Save the new workbook
new_workbook.save('test_graph.xlsx')