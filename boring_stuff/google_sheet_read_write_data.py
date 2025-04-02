import ezsheets

ss = ezsheets.createSpreadsheet('my spreadsheet')
sheet=ss[0]
print(sheet.title)

sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
print(sheet['A1'])
print(sheet['A2'])
print(sheet[2,1])

sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'Robocop'
ss.refresh()

print(ezsheets.convertAddress('A2'))
print(ezsheets.convertAddress(1,2))
print(ezsheets.getColumnNumberOf('B'))
print(ezsheets.getColumnLetterOf(999))
print(ezsheets.getColumnNumberOf('ZZZ'))