import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'C2'

wb.save('freezeExample.xlsx')
