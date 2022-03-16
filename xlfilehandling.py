import pandas as pd

file = pd.ExcelFile('/Users/Riibig5Techy/Projects/Python/crash_course/sales.xlsx')
print(file.sheet_names,'\n')
sales_sheet = file.parse('sales')
print(sales_sheet,'\n')
print(sales_sheet.Date,'\n')
print(type(sales_sheet),'\n')
print(sales_sheet.Amount.sum(),'\n')
print(sales_sheet.loc[0],'\n')
print(sales_sheet.loc[0,'Amount'],'\n')
sales_sheet.set_index('Customer', inplace=True)
print(sales_sheet.loc['MMC Inc.'],'\n')
sales_sheet.reset_index()
print(sales_sheet['Invoice'],'\n')
print(type(sales_sheet['Invoice']),'\n')

print(sales_sheet.loc[sales_sheet['Invoice']==99],'\n')
print(sales_sheet.loc[sales_sheet['Amount'] > 2000],'\n')