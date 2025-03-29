import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
# sheet['A1'].value = 'Hello world!'
sheet['A1'] = 'Hello world!'

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A5'].font = fontObj1
sheet['A5'] = 'Bold Times New Roman'

wb.save('styles.xlsx')
