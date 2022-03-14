import pandas as pd

file = pd.ExcelFile('/Users/Riibig5Techy/Projects/Python/crash_course/sales.xlsx')
print(file.sheet_names)
sales_sheet = file.parse('sales')
print(sales_sheet)
print(sales_sheet.Date)
print(type(sales_sheet))