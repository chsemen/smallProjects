import ezsheets

ss1 = ezsheets.createSpreadsheet('First Sheet')
ss2 = ezsheets.createSpreadsheet('Second Sheet')
print(ss1)

ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1[0].copyTo(ss2)
print(ss2.sheetTitles)
