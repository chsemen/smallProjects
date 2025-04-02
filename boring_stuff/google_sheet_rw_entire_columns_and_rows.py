import ezsheets

ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
print(sheet.getRow(1))
print(sheet.getRow(2))

print(sheet.getColumn(1))

print(sheet.getColumn('A'))

print(sheet.getRow(3))
sheet.updateRow(3, ['Pumkin', 11.50, '20', '230'])
print(sheet.getRow(3))

columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    columnOne[i] = value.upper()

sheet.updateColumn(1, columnOne)

rows = sheet.getRows()
print(rows[0])
print(rows[1])

rows[1][0] = 'PUMKIN'
print(rows[1])

print(rows[10])
rows[10][2] = 400
rows[10][3] = 904
print(rows[10])

sheet.updateRows(rows)

print(sheet.rowCount)
print(sheet.columnCount)

sheet.columnCount=4
print(sheet.columnCount)